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

##Generate Gate Lists
generic_list_large = np.linspace(0, 6.0, 61)
generic_list_medium = np.linspace(0, 3.0, 31)
generic_list_small = np.linspace(0, 2.0, 21)

large_resonance = [0.695, 2.0, 3.305,4.61,5.95]
medium_resonance = [-0.41, 1, 2.41]
small_resonance = []

large_gate = generic_list_large.tolist() + large_resonance
medium_gate = generic_list_medium.tolist() + medium_resonance
small_gate= generic_list_small.tolist() + small_resonance 

#large_gate_dyn = large_resonance + [1.2, 2.6, 3.6, 3.0, 5.6]
large_gate_dyn =  [0.695, 3.305, 4.61, 5.95] + [1.2, 2.6, 3.5, 3.0, 5.6]
medium_gate_dyn = medium_resonance + [0.3, 1.6, 4.0, 5.0]
small_gate_dyn = np.linspace(0, 2.0, 6)

#Dynamic
system_l025_dyn = {"l":0.25, "delta":0.025, "gate":small_gate_dyn , "frank":[0.0], "barrier":[0.05], 
               "operation":[], "A":0.3, "B":1, "C":7} 
system_l05_dyn = {"l":0.5, "delta":0.1,"gate":medium_gate_dyn , "frank":[0.0],"barrier":[0.2], 
              "operation":[], "A":0.3, "B":1, "C":7}  
system_l075_dyn = {"l":0.75, "delta":0.3, "gate":large_gate_dyn , "frank":[0.0], "barrier":[0.8], 
              "operation":[], "A":0.3, "B":1, "C":7}

configuration_dyn =[system_l025_dyn, system_l05_dyn, system_l075_dyn] 

### Stationary
system_l025_stat = {"l":0.25, "delta":0.025, "gate":small_gate , "frank":[0.0], "barrier":[0.05], 
        "operation":[], "A":0.1, "B":1, "C":7, "gate_start":-2.5, "gate_end":3.5, "gate_points":300}  
system_l05_stat = {"l":0.5, "delta":0.1,"gate":medium_gate , "frank":[0.0],"barrier":[0.2], 
        "operation":[], "A":0.1, "B":1, "C":7, "gate_start":-2.5, "gate_end":4.5, "gate_points":350} 
system_l075_stat = {"l":0.75, "delta":0.3, "gate":large_gate , "frank":[0.0], "barrier":[0.8], 
        "operation":[], "A":0.1, "B":1, "C":7, "gate_start":-2.5, "gate_end":6.5, "gate_points":450}

configuration_stat =[system_l025_stat, system_l05_stat, system_l075_stat] 

#With Fixed Point
#for configuration in [configuration_stat,configuration_dyn]:
#    for system in configuration:
#        human.create_switch_operation_fixed_start(system, 0.0)

for system in configuration_dyn:
    human.create_switch_operation(system)


# # Voltage off/on and off/on

#External Parameters
#temp =[293] 
#env =[0.0, 0.04] 
#bias = [0.2, 0.4, 0.8]


# In[8]:
#timestart = 0; timeend= 1e8; timegrid=1e5; clustertime_1 = "24:00:00"; cluster_1="lima"


# ## off -> on
########

# In[27]:

#project_offon = cluster.jobproject(name="off-on", program=program_rrze, programprojectpath=path_rrze  , projectpath=projectpath,
#				mode=20, summary_bool=1, performance_bool=0, pop_bool=1,  N=2000, coupling_bool=1,
#				pop_number=15, rhox_bool=1, plot_bool=1, meBND=6, meBND_small=6,xranges=2.0e0,
#				medim1=60,medim0=60, timebool=0, potential_id=0)


# In[28]:

#project_offon_rhox = cluster.jobproject(name="off-on_rhox", program=program_rrze, programprojectpath=path_rrze  , projectpath=projectpath,
#				mode=21, summary_bool=1, performance_bool=1, pop_bool=1,  N=2000, coupling_bool=1,
#				pop_number=15, rhox_bool=1, plot_bool=1, meBND=6, meBND_small=6,xranges=2.0e0,
#				medim1=60,medim0=60, timebool=0, potential_id=0)


# ## on--> off

# In[29]:

#project_onoff = cluster.jobproject(name="on-off", program=program_rrze, programprojectpath=path_rrze  , projectpath=projectpath,
#				mode=20, summary_bool=1, performance_bool=1, pop_bool=1,  N=2000, coupling_bool=1,
##				pop_number=15, rhox_bool=1, plot_bool=1, meBND=6, meBND_small=6,xranges=2.0e0,
#				medim1=60,medim0=60, timebool=0, potential_id=0)


# In[30]:

#project_onoff_rhox = cluster.jobproject(name="on-off_rhox", program=program_rrze, programprojectpath=path_rrze  , projectpath=projectpath,
#				mode=21, summary_bool=1, performance_bool=1, pop_bool=1,  N=2000, coupling_bool=1,
#				pop_number=15, rhox_bool=1, plot_bool=1, meBND=6, meBND_small=6,xranges=2.0e0,
#				medim1=60,medim0=60, timebool=0, potential_id=0)


# In[31]:

#project_offon_list = [project_offon, project_offon_rhox] 


# In[32]:

#project_onoff_list = [project_onoff, project_onoff_rhox] 


# In[ ]:

#for potential in configuration_dyn:
# for gate in potential["gate"]:
#  for frank in potential["frank"]:
#    for vb in potential["barrier"]:
#        
#	## Reservoir Parameters
#	    for b in bias:
#		for en in env:
#		    for T in temp:
##			
#			    string = ""
#			    string += human_readable_length(potential["l"])                                    
#			    string += "_G_" + str(gate) +  "_Vb_" + str(vb) + "_B_" + str(b)                                                                     
#			    string += human_readable_frank(frank)
#			    string += human_readable_temperature(T)
#			    string += human_readable_environment(env)
#			    
#			    for job in project_offon_list:
#				## OFF -> ON ### ### ### ### ### ### ### ### ##
#				## Job no rhox
#				job.add_job(
#
#				#ClusterSpeccs
#				cluster=cluster_1,
#				time = clustertime_1,
#
#				specific=string, 
#				grid_bias_voltage = 1,
#
#				## Timing 
#				time_start=timestart,
#				time_end = timeend,
#				time_grid = timegrid,
#
#				## Fixed for this Project
#				C= potential["C"],
#				A =  potential["A"], B= potential["B"],
#				l = potential["l"],
#				delta= potential["delta"],
#
#				beta2L = set_bath_by_temp(T), beta2R=set_bath_by_temp(T),
#
#				#Loop Variables
#				## Bias
#				start_bias_voltage=0.0,                                        
#				end_bias_voltage=b,
#
#				## Gate
#				start_gate_voltage=gate,
#				end_gate_voltage=gate,
#
#				Vb=vb,
#				xshift = frank,
#				T = T, hbath_temp=T,
#				eta = en)  
#				
#				
#			    for job in project_onoff_list:
#				## OFF -> ON ### ### ### ### ### ### ### ### ##
#				## Job no rhox
#				job.add_job(
#
#				#ClusterSpeccs
#				cluster=cluster_1,
#				time = clustertime_1,
#
#				specific=string, 
#				grid_bias_voltage = 1,
#
#				## Timing 
#				time_start=timestart,
#				time_end = timeend,
#				time_grid = timegrid,
#
#				## Fixed for this Project
#				C= potential["C"],
#				A =  potential["A"], B= potential["B"],
#				l = potential["l"],
#				delta= potential["delta"],
#
#				beta2L = set_bath_by_temp(T), beta2R=set_bath_by_temp(T),
#
#				#Loop Variables
#				## Bias
#				start_bias_voltage=b,                                        
#				end_bias_voltage=0.0,
#
#				## Gate
#				start_gate_voltage=gate,
#				end_gate_voltage=gate,
#
#				Vb=vb,
#				xshift = frank,
#				T = T, hbath_temp=T,
#				eta = en)      
#
#
## In[ ]:
#
#project_offon.put_runscript(); project_offon.put_jobproject()
#
#
## In[ ]:
#
#project_offon_rhox.put_runscript(); project_offon_rhox.put_jobproject()
#
#
## In[ ]:
#
#project_onoff.put_runscript(); project_onoff.put_jobproject()
#
#
## In[ ]:
#
#project_onoff_rhox.put_runscript(); project_onoff_rhox.put_jobproject()
#
#
## # Reine Zustaende
#
## In[ ]:
#
##External Parameters
#temp =[293, 10] 
#env =[0.0, 0.04] 
#bias = [0, 0.2, 0.4]
#
## Calc Paramters
#occupation =[0, 1] 
#states =[1,2] 
#
#
## In[ ]:
#
#timestart = 0; timeend= 1e8; timegrid=1e5; clustertime_2 = "24:00:00"; cluster_2="lima"
#
#
## In[ ]:
#
#project_pure = cluster.jobproject(name="pure", program=program_rrze, programprojectpath=path_rrze  , projectpath=projectpath,
#                                        mode=20, N=2000, summary_bool=1, performance_bool=1, pop_bool=1, coupling_bool=1,
#                                        pop_number=15, rhox_bool=1, plot_bool=1, meBND=6, meBND_small=6, xranges=2.0e0,
#                                        medim1=60,medim0=60, timebool=0, potential_id=0, initialstate=2)
#
#
## In[ ]:
#
#project_pure_rhox = cluster.jobproject(name="pure_rhox", program=program_rrze, programprojectpath=path_rrze  , projectpath=projectpath,
#                                        mode=20, N=2000, summary_bool=1, performance_bool=1, pop_bool=1, coupling_bool=1,
#                                        pop_number=5, evo_method=2, rhox_bool=1, plot_bool=1, meBND=6, meBND_small=6, xranges=2.0e0,
#                                        medim1=60,medim0=60, timebool=0, potential_id=0, initialstate=2)
#
#
## In[ ]:
#
#project_pure_list =[project_pure_rhox, project_pure] 
#
#
## In[ ]:
#
#for potential in configuration_dyn:
#    for gate in potential["gate"]:
#        for frank in potential["frank"]:
#            for vb in potential["barrier"]:
#                ## Reservoir Parameters
#                    for b in bias:
#                        for en in env:
#                            for T in temp:
#                                ## What States and Occupation
#                                for s in states:
#                                    for o in occupation:
#                                
#                                            string = ""
#                                            string += human_readable_length(potential["l"])                                    
#                                            string += "_G_" + str(gate) +  "_Vb_" + str(vb) + "_B_" + str(b) + "_S_" + str(s)                                                                  
#                                            string += human_readable_frank(frank)
#                                            string += human_readable_temperature(T)
#                                            string += human_readable_environment(env)
#                                            string += human_readable_occupation(o)
#
#
#                                            ### PURE PURE PURE PURE
#                                            ## Job no rhox
#                                            for jobs in project_pure_list:
#                                                jobs.add_job(
#
#                                                ## CLUSTER 
#                                                cluster=cluster_2,
#                                                time = clustertime_2,
#
#                                                specific=string, 
#                                                start_bias_voltage=b,
#                                                end_bias_voltage=b,
#                                                grid_bias_voltage = 1,
#
#                                                ## Timing 
#                                                time_start=timestart,
#                                                time_end = timeend,
#                                                time_grid = timegrid,
#
#                                                ## Fixed for this Project
#                                                C= potential["C"],
#                                                A =  potential["A"], B= potential["B"],
#                                                l = potential["l"],
#                                                delta= potential["delta"],
#                                                Vb=vb,
#                                                beta2L = set_bath_by_temp(T), beta2R=set_bath_by_temp(T),
#
#                                                #Loop Variables
#
#                                                start_gate_voltage=gate,
#                                                end_gate_voltage=gate,
#                                                xshift = frank,
#                                                T = T, hbath_temp=T,
#                                                eta = en, 
#
#                                                ### States
#                                                initial_state_number=s, 
#                                                initial_occupation = o
#
#                                                )
#
#
## In[ ]:
#
#project_pure.put_runscript();project_pure.put_jobproject()
#
#
## ## RHOX
#
## In[ ]:
#
#project_pure_rhox.put_runscript();project_pure_rhox.put_jobproject()


## Switching
##External Parameters
temp =[293] 
env =[0.0, 0.04] 
bias = [0.3]

## In[8]:
timestart = 0; timeend= 1e8; timegrid=1e6; clustertime_3 = "24:00:00"; cluster_3="emmy"

## In[9]:
project_switch = cluster.jobproject(name="switch", program=program_rrze, programprojectpath=path_rrze  , projectpath=projectpath,
                                        mode=20, N=3000, summary_bool=1, performance_bool=0, pop_bool=1, coupling_bool=0,
                                        pop_number=15, rhox_bool=0, plot_bool=1, meBND=5 , meBND_small=5,xranges=2.0e0,
                                        medim1=40, medim0=40, timebool=0, potential_id=0, initialstate=1)

#project_switch_lowT = cluster.jobproject(name="switch_lowT", program=program_rrze, programprojectpath=path_rrze, projectpath=projectpath,
#                                        mode=20, N=2000, summary_bool=1, performance_bool=0, pop_bool=1, coupling_bool=1,
#                                        pop_number=15, rhox_bool=1, plot_bool=1, meBND=5,meBND_small=5,xranges=2.0e0,
#                                        medim1=40, medim0=40, timebool=0, potential_id=0, initialstate=1)

#project_switch_rhox = cluster.jobproject(name="switch_rhox", program=program_rrze, programprojectpath=path_rrze  , projectpath=projectpath,
#                                        mode=21, N=2000, summary_bool=1, performance_bool=1, pop_bool=1, coupling_bool=1,
#                                        pop_number=15, rhox_bool=1, plot_bool=1, meBND=6,meBND_small=6,xranges=2.0e0,
#                                        medim1=60,medim0=60, timebool=0, potential_id=0, initialstate=1)
#
#
## In[11]:
project_switch_list =[project_switch] 

## In[12]:
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

#for job in project_switch_lowT.joblist:
#    job.beta2L = 0.01
#    job.beta2R = 0.01

#project_switch_lowT.put_jobproject()
#
#
## In[14]:
#
#project_switch_rhox.put_jobproject()
#
#
## # Stationary
#
## ## Gate Tester
#
## In[ ]:
#
gate_values = np.arange(-1, 6, 0.01)
#
#
## In[ ]:
#
gate_tester = [{"project":cluster.jobproject(name="Gate_tester_l" + str(potential["l"]) , program=program_rrze, programprojectpath=path_rrze , projectpath=projectpath,
                                        mode=4, summary_bool=1, performance_bool=0, pop_bool=0, coupling_bool=0,
                                        pop_number=50, N=2000, rhox_bool=0, plot_bool=1, meBND_small=5, meBND=5,xranges=2.0e0,
                                        medim1=40,medim0=40,timebool=0, potential_id=0), "potential":potential} for potential in configuration_stat ]


## In[ ]:
#
for project in gate_tester:    
    #Specific Potential
    for frank in project["potential"]["frank"]:
        for vb in project["potential"]["barrier"]:
            #Gate
            #for gate in gate_values:

                string = ""
                string += human.human_readable_length(project["potential"]["l"])                                    
                string += "_Vb_" + str(vb)                                                               
                string += human.human_readable_frank(frank)
                
                project["project"].add_job(
                
                specific=string,                    
                
                #Gate     
                start_gate_voltage=0.0, 
                end_gate_voltage=1.0, 
                grid_gate_voltage=1,
               
                #Bias 
                start_bias_voltage=-1,
                end_bias_voltage=6.5,
                grid_bias_voltage = 7,
                    
                ## Fixed for this Project
                C= project["potential"]["C"],
                A =  project["potential"]["A"], B= project["potential"]["B"],
                l = project["potential"]["l"],
                delta= project["potential"]["delta"],
                       
                #Loop Variables
                Vb=vb,
                xshift = frank,
                T = 293, hbath_temp=293,
                eta = 0.04
                )

for project in gate_tester:
    project["project"].put_jobproject()
    project["project"].put_runscript()

## # Current - Voltage - Characteristics Heatmap
##External Parameters
temp =[10, 293] 
env =[0.0, 0.04] 
#bias = [0.2, 0.4]
#
#
## In[ ]:
#
clustertime_cvc = "24:00:00"; cluster_cvc="lima"

project_paper_cvc_large = cluster.jobproject(name="Paper_job_cvc_large", program=program_rrze, programprojectpath=path_rrze , projectpath=projectpath,
                                        mode=3, summary_bool=1, performance_bool=1, pop_bool=0, coupling_bool=0, 
                                        potential_id=0,pop_number=20, N=3000, rhox_bool=0, plot_bool=1, meBND_small=5, meBND=5, xranges=2.0e0,
                                        medim1=40,medim0=40, timebool=0)
 
project_paper_cvc_medium = cluster.jobproject(name="Paper_job_cvc_medium", program=program_rrze, programprojectpath=path_rrze , projectpath=projectpath,
                                        mode=3, summary_bool=1, performance_bool=1, pop_bool=0, coupling_bool=0, 
                                        potential_id=0, pop_number=20, N=3000, rhox_bool=0, plot_bool=1, meBND_small=23, meBND=23, xranges=2.0e0,
                                        medim1=25,medim0=25, timebool=0)

project_paper_cvc_small = cluster.jobproject(name="Paper_job_cvc_small", program=program_rrze, programprojectpath=path_rrze , projectpath=projectpath,
                                        mode=3, summary_bool=1, performance_bool=1, pop_bool=0, coupling_bool=0, 
                                        potential_id=0, pop_number=20, N=3000, rhox_bool=0, plot_bool=1, meBND_small=10, meBND=10, xranges=2.0e0,
                                        medim1=15,medim0=15, timebool=0)

project_list_cvc = [project_paper_cvc_large, project_paper_cvc_medium, project_paper_cvc_small]

for potential in configuration_stat:
    for gate in potential["gate"]:
        for frank in potential["frank"]:
            for vb in potential["barrier"]:
                ## Reservoir Parameters
                    for b in bias:
                        for en in env:
                            for T in temp:
                                
                                    string = ""
                                    string += human.human_readable_length(potential["l"])                                    
                                    string += "_Vb_" + str(vb)                                                                
                                    string += human.human_readable_frank(frank)        
                                    string += human.human_readable_temperature(T)
                                    string += human.human_readable_environment(en)
                       
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
        
                                        #Loop Variables n  3 18:29 inputfile_switch_LARGE_G0.0_0.5_Vb_0.8_B_0.3_Switch_ON__ZeroS_T.inp_FeBo__ztimeVb=vb,
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

## # Slow Switch
#
## In[ ]:
#
##External Parameters
#temp =[10, 293] 
#env =[0.0, 0.04] 
#bias = [0.2, 0.4]
#
#
## In[ ]:
#
#time_slow = "3:00:00"; cluster_slow="lima"
#
#
## In[ ]:
#
#project_slowswitch_paper = cluster.jobproject(name="Paper_job_slow", program=program_rrze, programprojectpath=path_rrze , projectpath=projectpath,
#                                        mode=2, summary_bool=1, performance_bool=1, pop_bool=1, coupling_bool=1, 
#                                        potential_id=0, pop_number=20, N=1000, rhox_bool=1, plot_bool=1, meBND=6, xranges=2.0e0,
#                                        medim1=60,medim0=60, timebool=0)
#
#
## In[ ]:
#
#project_slowswitch_paper = cluster.jobproject(name="Paper_job_slow", program=program_rrze, programprojectpath=path_rrze , projectpath=projectpath,
#                                        mode=2, summary_bool=1, performance_bool=1, pop_bool=1, coupling_bool=1, 
#                                        potential_id=0, pop_number=20, N=1000, rhox_bool=1, plot_bool=1, meBND=6, xranges=2.0e0,
#                                        medim1=60,medim0=60, timebool=0)
#
#
## In[ ]:
#
#for potential in configuration_stat:
#        for frank in potential["frank"]:
#            for vb in potential["barrier"]:
#                ## Reservoir Parameters
#                    for b in bias:
#                        for en in env:
#                            for T in temp:
#                                
#                                    string = ""
#                                    string += human_readable_length(potential["l"])                                    
#                                    string += "_Vb_" + str(vb)                                                                
#                                    string += human_readable_frank(frank)        
#                                    string += human_readable_temperature(T)
#                                    string += human_readable_environment(env)
#                        
#                                    project_slowswitch_paper.add_job(
#                                    specific=string, 
#           
#                                    start_bias_voltage=0.2,
#                                    end_bias_voltage=0.4,
#                                    grid_bias_voltage = 1,
#                                
#                                    ## Cluster
#                                    cluster = cluster_slow, 
#                                    time = time_slow,
#                                                              
#
#                                    ## Fixed for this Project
#                                    C= potential["C"],
#                                    A =  potential["A"], B= potential["B"],
#                                    l = potential["l"],
#                                    delta= potential["delta"],
#                              
#                                    beta2L = set_bath_by_temp(T), beta2R=set_bath_by_temp(T),
#    
#                                    #Loop Variables
#                                    Vb=vb,
#                                    xshift = frank,
#                                    T = T, hbath_temp=T,
#                                    eta = en,
#
#                                    start_gate_voltage=0, 
#                                    end_gate_voltage=3,
#                                    grid_gate_voltage=600
#                                
#                                    )
#
#
## In[ ]:
#
#project_slowswitch_paper.put_jobproject()
#
#
## In[ ]:
#
#project_slowswitch_paper.put_runscript()
#
#
## # Diode
#
## In[ ]:
#
##External Parameters
#temp =[10, 293] 
#env =[0.0, 0.04] 
#bias = [0.2, 0.4]
#
##Angle
#angle =[0, 25, 60] 
#
#
## In[ ]:
#
#time_diode = "6:00:00"; cluster_diode="lima"
#
#
## In[ ]:
#
#project_diode_paper = cluster.jobproject(name="Paper_job_diode", program=program_rrze, programprojectpath=path_rrze , projectpath=projectpath,
#                                        mode=4, summary_bool=1, performance_bool=0, pop_bool=1, coupling_bool=1, surf_bool=0,
#                                        potential_id=10,pop_number=50, N=1000, rhox_bool=1, plot_bool=1, meBND=6,xranges=2.0e0,
#                                        medim1=60,medim0=60, timebool=0)
#
#
## In[ ]:
#
#for potential in configuration_stat:
#        for frank in potential["frank"]:
#            for vb in potential["barrier"]:
#                ## Reservoir Parameters
#                    for b in bias:
#                        for en in env:
#                            for T in temp:
#                                ## Further Parameteter
#                                for phi in angle:
#                                             
#                                    string = ""
#                                    string += human_readable_length(potential["l"])                                    
#                                    string += "_Vb_" + str(vb) + "_Phi_" + str(phi)                                                            
#                                    string += human_readable_frank(frank)        
#                                    string += human_readable_temperature(T)
#                                    string += human_readable_environment(env)
#                        
#                                    project_diode_paper.add_job(
#                                    specific=string, 
#           
#                                    start_bias_voltage=0,
#                                    end_bias_voltage=4.5,
#                                    grid_bias_voltage = 900,
#                                
#                                    ## Cluster
#                                    cluster = cluster_diode, 
#                                    time = time_diode, 
#                                
#                                    ## Diode Paramter
#                                    angle = phi, 
#                                    Lj = 1, 
#
#                                    ## Fixed for this Project
#                                    C= potential["C"],
#                                    A =  potential["A"], B= potential["B"],
#                                    l = potential["l"],
#                                    delta= potential["delta"],
#                              
#                                    beta2L = set_bath_by_temp(T), beta2R=set_bath_by_temp(T),
#    
#                                    #Loop Variables
#                                    Vb=vb,
#                                    xshift = frank,
#                                    T = T, hbath_temp=T,
#                                    eta = en,
#                                   
#                                    ## Gate
#                                    start_gate_voltage=0, 
#                                    end_gate_voltage= 1,
#                                    grid_gate_voltage=2)
#
#
## In[ ]:
#
#project_diode_paper.put_jobproject()
#
#
## In[ ]:
#
#project_diode_paper.put_runscript()
#
#
## # Barrier
#
## In[8]:
#
##External Parameters
#temp =[10, 293] 
#env =[0.0, 0.04] 
#bias = [0.2, 0.4]
#
##Angle
#barrier_diff =[-0.2,-0.1,0.1,0.2,0.3,0.4] 
#
#
## In[9]:
#
#cluster_barrier = "lima";time_barrier = "1:00:00"
#
#
## In[10]:
#
#project_paper_barrier = cluster.jobproject(name="Paper_barrier_cvc", program=program_rrze, programprojectpath=path_rrze , projectpath=projectpath,
#                                        mode=1, summary_bool=1, performance_bool=1, pop_bool=1, coupling_bool=1, 
#                                        potential_id=20,pop_number=20, N=2000, rhox_bool=1, plot_bool=1,meBND_small=10, meBND=10,xranges=2.0e0,
#                                        medim1=60,medim0=60, timebool=0)
#
#
## In[11]:
#
#for potential in configuration_stat:
#    for gate in potential["gate"]:
#        for frank in potential["frank"]:
#            for vb in potential["barrier"]:
#                for vb_diff in barrier_diff:
#                    ## Reservoir Parameters
#                    for b in bias:
#                        for en in env:
#                            for T in temp:
#                                
#                                    barrier_change = vb + vb_diff
#                                    
#                                    string = ""
#                                    string += human_readable_length(potential["l"])                                    
#                                    string += "_G_" + str(gate) +  "_Vb_" + str(vb)
#                                    string += human_readable_frank(frank)        
#                                    string += human_readable_temperature(T)
#                                    string += human_readable_environment(env)
#                                    string += human_readable_barrier_change(vb_diff)                     
#                                    
#                                    if barrier_change > 0:
#                                        
#                                        project_paper_barrier.add_job(
#                                        specific=string, 
#
#                                        start_bias_voltage=0,
#                                        end_bias_voltage=1.5,
#                                        grid_bias_voltage = 150,
#
#                                        ## Cluster
#                                        cluster = cluster_barrier, 
#                                        time = time_barrier,                
#
#                                        ## Fixed for this Project
#                                        C= potential["C"],
#                                        A =  potential["A"], B= potential["B"],
#                                        l = potential["l"],
#                                        delta= potential["delta"],
#
#
#                                        ##Second Set
#                                        l_2 = potential["l"], Vb_2 = barrier_change , 
#
#                                        ## Reservoir
#                                        beta2L = set_bath_by_temp(T), beta2R=set_bath_by_temp(T),
#
#                                        #Loop Variables
#                                        Vb=vb,
#                                        xshift = frank,
#                                        T = T, hbath_temp=T,
#                                        eta = en,
#
#                                        start_gate_voltage=gate, 
#                                        end_gate_voltage=gate
#                                        )
#
#
#project_paper_barrier.put_jobproject(); project_paper_barrier.put_runscript()

