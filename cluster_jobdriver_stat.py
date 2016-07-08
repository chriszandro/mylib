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
    projectpath = "/home/vault/mpet/mpet07/projects/NEW_set_cvc" + signature +"/"    
else:
    program_rrze =  "./gmaster13"
    path_rrze = "/user/chriz/calculations"
    projectpath =  "/user/chriz/calculations"    

small_gate=[]
medium_gate=[]
large_gate=[]

### Stationary
system_l025_stat = {"l":0.25, "delta":0.025, "gate":small_gate , "frank":[0.0], "barrier":[0.05], 
        "operation":[], "A":1.0, "B":1, "C":7, "gate_start":-2.5, "gate_end":3.5, "gate_points":300, "Sym":0.5}  
system_l05_stat = {"l":0.5, "delta":0.1,"gate":medium_gate , "frank":[0.0],"barrier":[0.2], 
        "operation":[], "A":1.0, "B":1, "C":7, "gate_start":-2.5, "gate_end":4.5, "gate_points":350, "Sym":1} 
system_l075_stat = {"l":0.75, "delta":0.3, "gate":large_gate , "frank":[0.0, 0.2, -0.2, 0.4, -0.4], "barrier":[0.8], 
        "operation":[], "A":0.1, "B":1, "C":7, "gate_start":-2.5, "gate_end":6.5, "gate_points":450, "Sym":2}

configuration_stat =[system_l075_stat, system_l05_stat, system_l025_stat]

## # Current - Voltage - Characteristics Heatmap
##External Parameters
temp =[293, 10] 
env =[0.0, 0.04, 1e-3] 

clustertime_cvc = "24:00:00"; cluster_cvc="lima"

project_paper_cvc_large = cluster.jobproject(name="Paper_job_cvc_large", program=program_rrze, programprojectpath=path_rrze , projectpath=projectpath,
                                        mode=3, summary_bool=1, performance_bool=0, pop_bool=0, coupling_bool=0, 
                                        potential_id=0,pop_number=20, N=3000, rhox_bool=0, plot_bool=0, meBND_small=5, meBND=5, xranges=2.0e0,
                                        medim1=40,medim0=40, timebool=0)
 
project_paper_cvc_medium = cluster.jobproject(name="Paper_job_cvc_medium", program=program_rrze, programprojectpath=path_rrze , projectpath=projectpath,
                                        mode=3, summary_bool=1, performance_bool=0, pop_bool=0, coupling_bool=0, 
                                        potential_id=0, pop_number=20, N=3000, rhox_bool=0, plot_bool=0, meBND_small=23, meBND=23, xranges=2.0e0,
                                        medim1=25,medim0=25, timebool=0)

project_paper_cvc_small = cluster.jobproject(name="Paper_job_cvc_small", program=program_rrze, programprojectpath=path_rrze , projectpath=projectpath,
                                        mode=3, summary_bool=1, performance_bool=0, pop_bool=0, coupling_bool=0, 
                                        potential_id=0, pop_number=20, N=3000, rhox_bool=0, plot_bool=0, meBND_small=10, meBND=10, xranges=2.0e0,
                                        medim1=15,medim0=15, timebool=0)

project_list_cvc = [project_paper_cvc_large, project_paper_cvc_medium, project_paper_cvc_small]

project_pair = [ [system_l075_stat, project_paper_cvc_large], [system_l05_stat, project_paper_cvc_medium], [system_l025_stat, project_paper_cvc_small] ]


for potential in configuration_stat:
   for frank in potential["frank"]:
        for vb in potential["barrier"]:
            for en in env:
                for T in temp:
                                    string = ""
                                    string += human.human_readable_length(potential["l"])                                    
                                    string += "_Vb_" + str(vb)                                                                
                                    string += human.human_readable_frank(frank)        
                                    string += human.human_readable_temperature(T)
                                    string += human.human_readable_environment(en)

                                    #Verification check

                                    print string
                       
                                    for project_cvc in project_list_cvc: 

                                        project_cvc.add_job(
                                        specific=string, 
                                        
                                        ##Gate
                                        start_gate_voltage = potential["gate_start"], 
                                        end_gate_voltage = potential["gate_end"],
                                        grid_gate_voltage =  potential["gate_points"],
                                       
                                        ##Bias 
                                        start_bias_voltage=0.0,
                                        end_bias_voltage=1.5,
                                        grid_bias_voltage = 1500,
                                        
                                        ## Cluster
                                        cluster = cluster_cvc, 
                                        time = clustertime_cvc,                
                                    
                                        ## Fixed for this Project
                                        C= potential["C"],
                                        A =  potential["A"], B= potential["B"],
                                        l = potential["l"],
                                        delta= potential["delta"],
                                  
                                        beta2L = human.set_bath_by_temp(T), beta2R=human.set_bath_by_temp(T),
        
                                        xshift = frank,
                                        T = T, hbath_temp=T,
                                        eta = en
                                        )


project_paper_cvc_small.put_jobproject()
project_paper_cvc_small.put_runscript()

project_paper_cvc_medium.put_jobproject()
project_paper_cvc_medium.put_runscript()

project_paper_cvc_large.put_jobproject()
project_paper_cvc_large.put_runscript()
