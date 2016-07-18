#### Preload 
import human_readable as human
import cluster
import math
import time
import os
import list_creator as list_creator
# import matplotlib.pyplot as plt
import analysis
from shutil import copyfile
from subprocess import call
import numpy as np

myhost = os.uname()[1]
signature = time.strftime("%d_%m")

### Might be obsolete
if myhost=="lima" or myhost=="cshpc":
    
    #Experimental
    program_rrze =  "./Release_Intel64_exp/gmaster13"
    path_rrze = "/home/hpc/mpet/mpet07/gmaster13"
    projectpath = "/home/vault/mpet/mpet07/projects/time/lima_NEW_set_time_non_stiff" + signature +"/"    

else:
    
    program_rrze =  "./gmaster13"
    path_rrze = "/user/chriz/expokit_heatmaps"
    projectpath =  "/user/chriz/expokit_heatmaps"    

#Switching Dynamic
system_l025_dyn = {"l":0.25, "delta":0.025, "gate":[] , "frank":[0.0], "barrier":[0.05], "gateonoff":[0.0,2.5,3.304],
        "operation":[], "A":0.1, "B":1, "C":7, "Sym":0.5} 
system_l05_dyn = {"l":0.5, "delta":0.1,"gate":[] , "frank":[0.0],"barrier":[0.2], "gateonoff":[0.0,2.5,3.304],
        "operation":[], "A":0.1, "B":1, "C":7, "Sym":1}  
system_l075_dyn = {"l":0.75, "delta":0.3, "gate":[] , "frank":[0.0], "barrier":[0.8], "gateonoff":[0.0,2.5,3.304],
        "operation":[], "A":0.1, "B":1, "C":7, "Sym":2}

potential = system_l075_dyn

#### Resources
computation = {"timestart":0,  "timeend":1e9, "timegrid":1e7, "clustertime":"24:00:00", "cluster":"emmy", 
     "program_rrze":"./Release_Intel64_exp/gmaster13",
     "path_rrze":"/user/chriz/gmaster13",
     "projectpath":"/user/chriz/expokit_heatmaps/"}

timestart = computation["timestart"];
timeend = computation["timeend"]; 
timegrid=computation["timegrid"]; 
clustertime_3 = computation["clustertime"];
cluster_3=computation["cluster"] 
program_rrze = computation["program_rrze"]; 
path_rrze = computation["path_rrze"]; 
projectpath = computation["projectpath"]

## Switching
##External Parameters
T=293
en = 0.001
bias = 0.30

large_resonance_plus = [0.695, 2.0, 3.305,4.61,5.95]
large_resonance_minus = [-3.2, -1.95, -0.61]

#-----Close to the Resonances with paramter +- "close_paramter"
close_paramter = 0.025
large_resonance_close = []

for number in large_resonance_plus: 
    large_resonance_close.append(number + close_paramter) 
    large_resonance_close.append(number - close_paramter) 
    large_resonance_close.append(number + 2*close_paramter) 
    large_resonance_close.append(number - 2*close_paramter) 

#Gate Preparation 
gate_start = 0.0
gate_end_list = np.linspace(1,7,600).tolist()  +  list_creator.resonance_refinement(large_resonance_plus, width=0.052, resolution=15)

print len(gate_end_list)
time.sleep(3)

enumrator=0
print gate_end_list
grid_time = 710
grid_gate = len(gate_end_list)

current_matrix = np.zeros(shape=(grid_gate, grid_time))
position_matrix = np.zeros(shape=(grid_gate, grid_time))
energy_matrix = np.zeros(shape=(grid_gate, grid_time))

for gate_end in gate_end_list: 
  

    # string = ""
    # string += human.human_readable_length(potential["l"])                                    
    # string += "_G" + str(gate_start)+ "_"+ str(gate_end) 
    # string += str(potential["barrier"] + "_B_" + str(bias)
    # string += human.human_readable_temperature(T)
    # string += human.human_readable_environment(en)

    computation = cluster.jobproject(name="switch", program=program_rrze, programprojectpath=path_rrze  , projectpath=projectpath,
                                            mode=40, N=3000, summary_bool=1, performance_bool=0, pop_bool=0, coupling_bool=0,
                                            pop_number=15, rhox_bool=0, plot_bool=1, meBND=5 , meBND_small=5,xranges=2.0e0,
                                            medim1=40, medim0=40, timebool=0, potential_id=0, initialstate=1)

    inputfile = computation.add_job(

    ## CLUSTER 
    cluster=cluster_3,
    time = clustertime_3,

    ## Timing 
    time_start = grid_time,
    time_end = grid_time,
    time_grid = grid_time,

    ## Bias
    specific="test", 
    start_bias_voltage=bias,
    end_bias_voltage=bias,

    #SWITCHING
    start_gate_voltage=gate_start,
    end_gate_voltage=gate_end,
    grid_bias_voltage = 1,


    ## Fixed for this Project
    C= potential["C"],
    A =  potential["A"], B= potential["B"],
    l = potential["l"],
    delta= potential["delta"],
    Vb=potential["barrier"][0],

    beta2L = human.set_bath_by_temp(T), beta2R=human.set_bath_by_temp(T),

    #Loop Variables
    xshift = potential["frank"][0],
    T = T, hbath_temp=T,
    eta = en)

    computation.put_jobproject()

    file_path = computation.get_files_fullpath()
    result_path = computation.get_result_fullpath()
    computation_file = computation.get_computation_file()

    print (computation_file)
    print ("inputfile", inputfile) 
    print ("filepath", file_path)

    os.chdir(projectpath + "switch/jobfiles")
    os.system("ls -l")

    execute = "./gmaster13" + " " + "inputfile_switchtest.inp" + " " + computation_file 
    os.system(execute)

    # Grap Data
    path = "/user/chriz/Dropbox/expokit_work1_1/"
    if not os.path.exists(path):
        os.makedirs(path)

    result_evo = "/user/chriz/expokit_heatmaps/switch/result/inputfile_switchtest.inp_FeBo__exptime.evo"

    # Einzelfiles
    copyfile(result_evo, path + "inputfile_switchtest_" + str(gate_end) + "_.evo") 

    system = analysis.system(computation_data=result_evo)
 
    current_matrix[enumrator] = system.current.T
    position_matrix[enumrator] = system.position.T
    energy_matrix[enumrator] = system.energy.T


    enumrator += 1

np.savetxt(path + "current.cum", current_matrix) 
np.savetxt(path + "position.pom", position_matrix) 
np.savetxt(path + "energy.enm", energy_matrix) 

np.savetxt(path + "time.grid", system.parameter) 
np.savetxt(path + "gate.grid", gate_end_list) 




