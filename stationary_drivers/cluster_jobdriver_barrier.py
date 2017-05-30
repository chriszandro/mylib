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


small_gate=[]
medium_gate=[]
large_gate=[]

system_l025_stat = {"l":0.25, "delta":0.025, "gate":small_gate , "frank":[0.0], "barrier":[0.05], 
        "operation":[], "A":1.0, "B":1, "C":7, "gate_start":-2.5, "gate_end":3.5, "gate_points":300, "Sym":0.5}  
system_l05_stat = {"l":0.5, "delta":0.1,"gate":medium_gate , "frank":[0.0],"barrier":[0.2], 
        "operation":[], "A":1.0, "B":1, "C":7, "gate_start":-2.5, "gate_end":4.5, "gate_points":350, "Sym":1} 
system_l075_stat = {"l":0.75, "delta":0.3, "gate":large_gate , "frank":[0.0, 0.2, -0.2, 0.4, -0.4], "barrier":[0.8], 
        "operation":[], "A":1.0, "B":1, "C":7, "gate_start":-2.5, "gate_end":6.5, "gate_points":450, "Sym":2}


configuration_stat =[system_l075_stat] 

#External Parameters
temp =[293] 
env =[0.04] 

#Diff
barrier_diff =[-0.3,-0.1,0.1,0.3] 

cluster_barrier = "lima";time_barrier = "12:00:00"


project_paper_barrier = cluster.jobproject(name="Paper_barrier_cvc", program=program_rrze, programprojectpath=path_rrze , projectpath=projectpath,
                                       mode=3, summary_bool=1, performance_bool=0, pop_bool=0, coupling_bool=1, 
                                       potential_id=20,pop_number=15, N=2000, rhox_bool=0, plot_bool=1, meBND_small=5, meBND=5,xranges=2.0e0,
                                       medim1=40,medim0=40, timebool=0)


for potential in configuration_stat:
       for frank in potential["frank"]:
           for vb in potential["barrier"]:
               for vb_diff in barrier_diff:
                   ## Reservoir Parameters
                       for en in env:
                           for T in temp:
                               
                                   barrier_change = vb + vb_diff
                                   
                                   string = ""
                                   string += human.human_readable_length(potential["l"])                                    
                                   string += "_Vb_" + str(vb)
                                   string += human.human_readable_frank(frank)        
                                   string += human.human_readable_temperature(T)
                                   string += human.human_readable_environment(en)
                                   string += human.human_readable_barrier_change(vb_diff)                     
                                   
                                   if barrier_change > 0:
                                       
                                       project_paper_barrier.add_job(
                                       specific=string, 

                                       start_bias_voltage=0.0,
                                       end_bias_voltage=2.0,
                                       grid_bias_voltage = 2000,

                                       # Cluster
                                       cluster = cluster_barrier, 
                                       time = time_barrier,                

                                       ## Fixed for this Project
                                       C= potential["C"],
                                       A =  potential["A"], B= potential["B"],
                                       l = potential["l"],
                                       delta= potential["delta"],


                                       ##Second Set
                                       l_2 = potential["l"], Vb_2 = barrier_change , 

                                       ## Reservoir
                                       beta2L = human.set_bath_by_temp(T), beta2R = human.set_bath_by_temp(T),

                                       #Loop Variables
                                       Vb=vb,
                                       xshift = frank,
                                       T = T, hbath_temp=T,
                                       eta = en,

                                        ##Gate
                                        start_gate_voltage = potential["gate_start"], 
                                        end_gate_voltage = potential["gate_end"],
                                        grid_gate_voltage =  potential["gate_points"]
                                       )


project_paper_barrier.put_jobproject(); project_paper_barrier.put_runscript()
