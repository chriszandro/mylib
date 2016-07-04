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
    program_rrze =  "./gmaster14"
    path_rrze = "/user/chriz/calculations"
    projectpath =  "/user/chriz/calculations"    

large_resonance = [-3.2, -1.9,0.695, 2.0, 3.305,4.61,5.95]
medium_resonance = [-0.41, 1, 2.41]
small_resonance = []

large_resonance_in_between = [1.35, 2.65, 0, 3.95, -1.26, 5.26, -2.6]
medium_resonance_in_between = [1.7, 0.3]
small_resonance_in_between = []

large_gate_dyn = large_resonance + large_resonance_in_between
medium_gate_dyn = medium_resonance + medium_resonance_in_between
small_gate_dyn = small_resonance + small_resonance_in_between

#### Neu Large Gate Dyn
large_gate_dyn = [2.0, 2.1, 1.9, 2.2, 1.8, 3.3, 2.65]

#Switching Dynamic
system_l025_dyn = {"l":0.25, "delta":0.025, "gate":small_gate_dyn , "frank":[0.0], "barrier":[0.05], "gateonoff":[0.0,2.5,3.304],
        "operation":[], "A":0.1, "B":1, "C":7, "Sym":0.5} 
system_l05_dyn = {"l":0.5, "delta":0.1,"gate":medium_gate_dyn , "frank":[0.0],"barrier":[0.2], "gateonoff":[0.0,2.5,3.304],
        "operation":[], "A":0.1, "B":1, "C":7, "Sym":1}  
system_l075_dyn = {"l":0.75, "delta":0.3, "gate":large_gate_dyn , "frank":[0.0], "barrier":[0.8], "gateonoff":[0.0,2.5,3.304],
        "operation":[], "A":0.1, "B":1, "C":7, "Sym":2}

configuration_dyn = [system_l075_dyn]

#Reine Zustaende
#------External Parameters
temp =[293] 
env =[1e-3] 
bias = [0, 0.3, 1.5]

#------Calc Paramters
occupation =[0] 
states =[1,2,7,8,9,10] 

timestart = 0; timeend= 1e9; timegrid=1e6; clustertime_2 = "24:00:00"; cluster_2="emmy"

project_pure = cluster.jobproject(name="pure", program=program_rrze, programprojectpath=path_rrze  , projectpath=projectpath,
                                        mode=20, N=2000, summary_bool=1, performance_bool=0, pop_bool=1, coupling_bool=0,
                                        pop_number=15, rhox_bool=0, plot_bool=1, meBND=5, meBND_small=5, xranges=2.0e0,
                                        medim1=40,medim0=40, timebool=0, potential_id=0, initialstate=2)

# project_pure_rhox = cluster.jobproject(name="pure_rhox", program=program_rrze, programprojectpath=path_rrze  , projectpath=projectpath,
                                        # mode=20, N=2000, summary_bool=0, performance_bool=0, pop_bool=1, coupling_bool=0,
                                        # pop_number=5, evo_method=2, rhox_bool=1, plot_bool=1, meBND=5, meBND_small=5, xranges=2.0e0,
                                        # medim1=40,medim0=40, timebool=0, potential_id=0, initialstate=2)


project_pure_list =[project_pure] 

for potential in configuration_dyn:
    for gate in potential["gate"]:
        for frank in potential["frank"]:
            for vb in potential["barrier"]:
                ## Reservoir Parameters
                    for b in bias:
                        for en in env:
                            for T in temp:
                                ## What States and Occupation
                                for s in states:
                                    for o in occupation:
                                
                                            string = ""
                                            string += human.human_readable_length(potential["l"])                                    
                                            string += "_G_" + str(gate) +  "_Vb_" + str(vb) + "_B_" + str(b) + "_S_" + str(s)                                                                  
                                            string += human.human_readable_frank(frank)
                                            string += human.human_readable_temperature(T)
                                            string += human.human_readable_environment(en)
                                            string += human.human_readable_occupation(o)


                                            ### PURE PURE PURE PURE
                                            ## Job no rhox
                                            for jobs in project_pure_list:
                                                jobs.add_job(

                                                ## CLUSTER 
                                                cluster=cluster_2,
                                                time = clustertime_2,

                                                specific=string, 
                                                start_bias_voltage=b,
                                                end_bias_voltage=b,
                                                grid_bias_voltage = 1,

                                                ## Timing 
                                                time_start=timestart,
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

                                                start_gate_voltage=gate,
                                                end_gate_voltage=gate,
                                                xshift = frank,
                                                T = T, hbath_temp=T,
                                                eta = en, 

                                                ### States
                                                initial_state_number=s, 
                                                initial_occupation = o

                                                )

project_pure.put_runscript();project_pure.put_jobproject() 
# project_pure_rhox.put_runscript();project_pure_rhox.put_jobproject() 




