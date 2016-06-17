#### Preload 
import human_readable as human
import cluster
import numpy as np
import math
import time
import os
myhost = os.uname()[1]
signature = time.strftime("%d_%m")

if myhost=="lima" or myhost=="cshpc":
    program_rrze =  "./Release_Intel64/gmaster13"
    path_rrze = "/home/hpc/mpet/mpet07/gmaster13"
    projectpath = "/home/vault/mpet/mpet07/projects/NEW_set_" + signature +"/"    
else:
    program_rrze =  "./gmaster13"
    path_rrze = "/user/chriz/calculations"
    projectpath =  "/user/chriz/calculations"    

##### List Generation
#-----Equally Spaced List
generic_list_large = np.linspace(0, 6.0, 61)
generic_list_medium = np.linspace(0, 3.0, 31)
generic_list_small = np.linspace(0, 2.0, 21)

#-----Resonaces in the systems
large_resonance = [-3.2, -1.95, -0.61, 0.695, 2.0, 3.305,4.61,5.95]
medium_resonance = [-0.41, 1, 2.41]
small_resonance = []

#-----Close to the Resonances with paramter +-"close_paramter"
close_paramter = 0.1

large_resonance_close = []
medium_resonance_close = []
small_resonance_close = []

for number in large_resonance: 
    large_resonance_close.append(number + close_paramter) 
    large_resonance_close.append(number - close_paramter) 

#----Exactly betwen the Resoances
large_resonance_in_between = [1.35, 2.65, 0, 3.95, -1.26, 5.26, -2.6]
medium_resonance_in_between = [1.7, 0.3]
small_resonance_in_between = []

#----Non Barrier Switching
large_resonance_non_barrier = [6.5, -3.0]
medium_resonance_non_barrier = [   ]
small_resonance_non_barrier = [   ]

###Listen Zusammenbauen
# large_gate_dyn = large_resonance + large_resonance_in_between 
# medium_gate_dyn = medium_resonance + medium_resonance_in_between 
# small_gate_dyn = np.linspace(0, 2.0, 6)

large_gate_dyn = large_resonance
medium_gate_dyn = medium_resonance + medium_resonance_in_between 
small_gate_dyn = np.linspace(0, 2.0, 6)


# Testing Lists
# large_gate_dyn =  [1.0, 3.0]

#### Print lists for verification
print "Large"
print large_gate_dyn
print "Medium"
print medium_gate_dyn 
print "Small"
print small_gate_dyn 


#Switching Dynamic
system_l025_dyn = {"l":0.25, "delta":0.025, "gate":small_gate_dyn , "frank":[0.0], "barrier":[0.05], "gateonoff":[0.0,2.5,3.304],
        "operation":[], "A":0.1, "B":1, "C":7, "Sym":0.5} 
system_l05_dyn = {"l":0.5, "delta":0.1,"gate":medium_gate_dyn , "frank":[0.0],"barrier":[0.2], "gateonoff":[0.0,2.5,3.304],
        "operation":[], "A":0.1, "B":1, "C":7, "Sym":1}  
system_l075_dyn = {"l":0.75, "delta":0.3, "gate":large_gate_dyn , "frank":[0.0], "barrier":[0.8], "gateonoff":[0.0,2.5,3.304],
        "operation":[], "A":0.1, "B":1, "C":7, "Sym":2}

configuration_dyn =[system_l075_dyn] 

for system in configuration_dyn:
    human.create_switch_operation_around_symmetric(system, system["Sym"])


## Switching
##External Parameters
temp =[293] 
env =[0.0, 0.04] 
bias = [0.3]

timestart = 0; timeend= 1e9; timegrid=1e6; clustertime_3 = "24:00:00"; cluster_3="emmy"

project_switch = cluster.jobproject(name="switch", program=program_rrze, programprojectpath=path_rrze  , projectpath=projectpath,
                                        mode=20, N=3000, summary_bool=1, performance_bool=0, pop_bool=1, coupling_bool=0,
                                        pop_number=15, rhox_bool=0, plot_bool=1, meBND=5 , meBND_small=5,xranges=2.0e0,
                                        medim1=40, medim0=40, timebool=0, potential_id=0, initialstate=1)

project_switch_specc2 = cluster.jobproject(name="switch_specc2", program=program_rrze, programprojectpath=path_rrze  , projectpath=projectpath,
                                        mode=20, N=2000, summary_bool=1, performance_bool=0, pop_bool=1, coupling_bool=0,
                                        pop_number=15, rhox_bool=0, plot_bool=1, meBND=5 , meBND_small=5,xranges=2.0e0,
                                        medim1=40, medim0=40, timebool=0, potential_id=0, initialstate=1)

project_switch_specc3 = cluster.jobproject(name="switch_specc3", program=program_rrze, programprojectpath=path_rrze  , projectpath=projectpath,
                                        mode=20, N=3000, summary_bool=1, performance_bool=0, pop_bool=1, coupling_bool=0,
                                        pop_number=15, rhox_bool=0, plot_bool=1, meBND=10 , meBND_small=10,xranges=2.0e0,
                                        medim1=60, medim0=60, timebool=0, potential_id=0, initialstate=1)

#project_switch_lowT = cluster.jobproject(name="switch_lowT", program=program_rrze, programprojectpath=path_rrze, projectpath=projectpath,
#                                        mode=20, N=2000, summary_bool=1, performance_bool=0, pop_bool=1, coupling_bool=1,
#                                        pop_number=15, rhox_bool=1, plot_bool=1, meBND=5,meBND_small=5,xranges=2.0e0,
#                                        medim1=40, medim0=40, timebool=0, potential_id=0, initialstate=1)

#project_switch_rhox = cluster.jobproject(name="switch_rhox", program=program_rrze, programprojectpath=path_rrze  , projectpath=projectpath,
#                                       mode=20, N=3000, summary_bool=1, performance_bool=0, pop_bool=1, coupling_bool=0,
#                                       pop_number=15, rhox_bool=1, plot_bool=1, meBND=5,meBND_small=5,xranges=2.0e0,
#                                       medim1=40,medim0=40, timebool=0, potential_id=0, initialstate=1)

project_switch_list =[project_switch, project_switch_specc3, project_switch_specc2] 

for potential in configuration_dyn:
        for frank in potential["frank"]:
           for vb in potential["barrier"]:
                #Switch Operations
                for operation in potential["operation"]:      
                    ## Reservoir Parameters
                         for b in bias:
                            for en in env:
                                for T in temp:
                           
                                    string = ""
                                    string += human.human_readable_length(potential["l"])                                    
                                    string += "_G" + str(operation["gate_init"])+ "_"+ str(operation["gate_final"]) 
                                    string += "_Vb_" + str(vb) + "_B_" + str(b)
                                    string += human.human_readable_switch_operation(operation["gate_init"],operation["gate_final"])
                                    string += human.human_readable_frank(frank)
                                    string += human.human_readable_temperature(T)
                                    string += human.human_readable_environment(en)


                                    ### SWITCH PURE
                                    ## Job no rhox
                                    for job in project_switch_list:
                                        job.add_job(

                                        ## CLUSTER 
                                        cluster=cluster_3,
                                        time = clustertime_3,

                                        ## Bias
                                        specific=string, 
                                        start_bias_voltage=b,
                                        end_bias_voltage=b,

                                        #SWITCHING
                                        start_gate_voltage=operation["gate_init"],
                                        end_gate_voltage=operation["gate_final"],
                                        grid_bias_voltage = 1,

                                        ## Timing 
                                        time_start = timestart,
                                        time_end = timeend,
                                        time_grid = timegrid,

                                        ## Fixed for this Project
                                        C= potential["C"],
                                        A =  potential["A"], B= potential["B"],
                                        l = potential["l"],
                                        delta= potential["delta"],
                                        Vb=vb,
                                        beta2L = human.set_bath_by_temp(T), beta2R=human.set_bath_by_temp(T),

                                        #Loop Variables
                                        xshift = frank,
                                        T = T, hbath_temp=T,
                                        eta = en)
project_switch.put_jobproject()
project_switch_specc2.put_jobproject()
project_switch_specc3.put_jobproject()

#for job in project_switch_lowT.joblist:
#    job.beta2L = 0.01
#    job.beta2R = 0.01

#project_switch_lowT.put_jobproject()
#
#roject_switch_rhox.put_jobproject()
