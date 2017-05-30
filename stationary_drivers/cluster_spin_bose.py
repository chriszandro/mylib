import human_readable as human
import cluster as cluster 
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

### Dynamic
system_normal_bare = {"l":0.5, "delta":0.1, "gate":[1.0] , "frank":[0, -0.3], "barrier":[0.2, 0.5], 
        "operation":[], "A":1.0, "B":1.0, "C":7, "spec":"_bare"}  
system_large_bare ={"l":0.8, "delta":0.1,"gate":[0.6] , "frank":[0.0],"barrier":[0.5, 0.2], 
              "operation":[], "A":1.0, "B":1.0, "C":7, "spec":"_bare"}  

system_normal_switch = {"l":0.5, "delta":0.1, "gate":[1.0] , "frank":[0.0], "barrier":[0.2, 0.5], 
               "operation":[], "A":0.1, "B":1.0, "C":7, "spec":"_switch"}  
system_large_switch ={"l":0.8, "delta":0.1,"gate":[0.6] , "frank":[0.0],"barrier":[0.5, 0.2], 
              "operation":[], "A":0.1, "B":1.0, "C":7, "spec":"_switch"}  

#configuration =[system_large_bare_switch, system_normal_bare_switch, system_large_bare, system_normal_bare] 
configuration =[system_normal_bare, system_normal_switch] 
#configuration =[system_normal_switch, system_normal_bare, system_large_bare, system_large_switch] 


timestart = 0; timeend= 1e8; timegrid=1e5; clustertime = "24:00:00"; clustername="lima"

project_spin_hbath = cluster.jobproject(name="spin-boson-hbath", program=program_rrze, programprojectpath=path_rrze  , projectpath=projectpath,
			mode=1, summary_bool=1, performance_bool=0, pop_bool=1,  N=2000, coupling_bool=1,
			pop_number=10, rhox_bool=1, plot_bool=1, meBND=6, meBND_small=6,xranges=2.0e0,
			medim1=60,medim0=60, timebool=0, potential_id=0, initialstate=3)

##Right Localized
project_spin_right = cluster.jobproject(name="spin-boson-right", program=program_rrze, programprojectpath=path_rrze  , projectpath=projectpath,
			mode=20, summary_bool=1, performance_bool=0, pop_bool=1,  N=2000, coupling_bool=1,
			pop_number=15, rhox_bool=1, plot_bool=1, meBND=6, meBND_small=6,xranges=2.0e0,
			medim1=60,medim0=60, timebool=0, potential_id=0, initialstate=4)
project_spin_right_rhox = cluster.jobproject(name="spin-boson-right-rhox", program=program_rrze, programprojectpath=path_rrze  , projectpath=projectpath,
			mode=21, summary_bool=1, performance_bool=0, pop_bool=1,  N=2000, coupling_bool=1,
			pop_number=15, rhox_bool=1, plot_bool=1, meBND=6, meBND_small=6,xranges=2.0e0,
			medim1=60,medim0=60, timebool=0, potential_id=0, initialstate=4)

##Left Localized
project_spin_left = cluster.jobproject(name="spin-left-boson", program=program_rrze, programprojectpath=path_rrze  , projectpath=projectpath,
			mode=20, summary_bool=1, performance_bool=0, pop_bool=1,  N=2000, coupling_bool=1,
			pop_number=15, rhox_bool=1, plot_bool=1, meBND=6, meBND_small=6,xranges=2.0e0,
			medim1=60,medim0=60, timebool=0, potential_id=0, initialstate=3)
project_spin_left_rhox = cluster.jobproject(name="spin-boson-left-rhox", program=program_rrze, programprojectpath=path_rrze  , projectpath=projectpath,
			mode=21, summary_bool=1, performance_bool=0, pop_bool=1,  N=2000, coupling_bool=1,
			pop_number=15, rhox_bool=1, plot_bool=1, meBND=6, meBND_small=6,xranges=2.0e0,
			medim1=60,medim0=60, timebool=0, potential_id=0, initialstate=3)

## Jobs
project_list_spin = [project_spin_left, project_spin_left_rhox, project_spin_right, project_spin_right_rhox, project_spin_hbath]

#External Parameters
temp =[5, 293] 
env =[0.0, 1e-3, 1e-4] 
fermion = [0.01]
bias = [0, 0.1, 0.2, 0.4]
occupation = [0]

for potential in configuration:
 for gate in potential["gate"]:
  for frank in potential["frank"]:
    for vb in potential["barrier"]:
        
## Reservoir Parameters
	    for b in bias:
               for ferm in fermion:
		  for en in env:
		    for T in temp:
                        for o in occupation:
			
			    string = ""
			    string += human.human_readable_length(potential["l"])                                    
			    string += "_G_" + str(gate) +  "_Vb_" + str(vb) + "_B_" + str(b) + potential["spec"]
                            string += human.human_readable_frank(frank)
                            string += human.human_readable_temperature(T)
			    string += human.human_readable_fermion(ferm)
			    string += human.human_readable_environment(en)
                            string += human.human_readable_occupation(o)
			    
			    for job in project_list_spin:
				job.add_job(

				#ClusterSpeccs
				cluster=clustername,
				time = clustertime,

				specific=string, 
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

				beta2L = ferm, beta2R=ferm,

				#Loop Variables
				## Bias
				start_bias_voltage=b,                                        
				end_bias_voltage=b,

				## Gate
				start_gate_voltage=gate,
				end_gate_voltage=gate,

				Vb=vb,
				xshift = frank,
				T = T, hbath_temp=T,
				eta = en, 
                                
                                #Preperation
                                initial_state_number=2, 
                                initial_state_number_2=1, 
                                initial_occupation=o
                                )  

for job in project_list_spin:
    job.put_jobproject()
    job.put_runscript()
