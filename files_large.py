# vim: set sw=4 ts=4 sts=4 et tw=78 foldmarker={,} foldlevel=0 foldmethod=marker:
import numpy as np


#L A R G E {
file_large_heatmap_T='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_large/result/inputfile_Paper_job_cvc_large_LARGE_Vb_0.8_ZeroS_T.inp_FeBo__heatmap_heatmap.cum'
file_large_heatmap='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_large/result/inputfile_Paper_job_cvc_large_LARGE_Vb_0.8_ZeroS.inp_FeBo__heatmap_heatmap.cum'
file_large_heatmap_pos_T='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_large/result/inputfile_Paper_job_cvc_large_LARGE_Vb_0.8_ZeroS_T.inp_FeBo__heatmap_heatmap.pom'
file_large_heatmap_pos='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_large/result/inputfile_Paper_job_cvc_large_LARGE_Vb_0.8_ZeroS.inp_FeBo__heatmap_heatmap.pom'

## With Environment
file_large_heatmap_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_large/result/inputfile_Paper_job_cvc_large_LARGE_Vb_0.8_ZeroS_env.inp_FeBo__heatmap_heatmap.cum'

file_large_heatmap_T_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_large/result/inputfile_Paper_job_cvc_large_LARGE_Vb_0.8_ZeroS_T_env.inp_FeBo__heatmap_heatmap.cum'

file_large_heatmap_pos_T_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_large/result/inputfile_Paper_job_cvc_large_LARGE_Vb_0.8_ZeroS_env_T.inp_FeBo__heatmap_heatmap.pom'

file_large_heatmap_pos_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_large/result/inputfile_Paper_job_cvc_large_LARGE_Vb_0.8_ZeroS_env.inp_FeBo__heatmap_heatmap.pom'


### GRID # {
file_large_prim='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_large/result/inputfile_Paper_job_cvc_large_LARGE_Vb_0.8_ZeroS_env.inp_FeBo_primary.grid'
file_large_sec='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_large/result/inputfile_Paper_job_cvc_large_LARGE_Vb_0.8_ZeroS_env.inp_FeBo_secondary.grid'

# }

#### Dia File {
file_large_dia='/home/vault/mpet/mpet07/projects/paper/switching/inputfile_weak_switching.inp_FeBo__switchmod_bias_at0.000.dia'
large_dia = np.loadtxt(file_large_dia)
## }
### Population {
#### No Environment {

file_large_heatmap_pop_T_array=[]
for i in range(1,11):
    file_large_heatmap_pop_T_array.append('/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_large/result/inputfile_Paper_job_cvc_large_LARGE_Vb_0.8_ZeroS_T.inp_FeBo__heatmap_occ_'+str(i)+'_heatmap_state.pop')

## }

 #No Temperature { 

file_large_heatmap_pop_array=[]
for i in range(1,11):
    file_large_heatmap_pop_array.append('/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_large/result/inputfile_Paper_job_cvc_large_LARGE_Vb_0.8_ZeroS.inp_FeBo__heatmap_occ_'+str(i)+'_heatmap_state.pop')
  # } 
# Population end }

# LARGE END }

##########################################################################################################################################
#MEDIUM {
#########################################################################################################################################
### Resonances {
medium_symmetrie = [1]
medium_resonances = [-0.41, 2.41]
#}
#### Dia File {
file_medium_dia='/home/vault/mpet/mpet07/projects/paper/switching/inputfile_strong_switching.inp_FeBo__switchmod_bias_at0.000.dia'
medium_dia = np.loadtxt(file_medium_dia)
## }
file_medium_heatmap_T='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T.inp_FeBo__heatmap_heatmap.cum'

file_medium_heatmap='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS.inp_FeBo__heatmap_heatmap.cum'

file_medium_heatmap_pos_T='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T.inp_FeBo__heatmap_heatmap.pom'

file_medium_heatmap_pos='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS.inp_FeBo__heatmap_heatmap.pom'

### Population {

# Population NO Environment NO Temperature {
file_medium_heatmap_pop_T_1='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T.inp_FeBo__heatmap_occ_1_heatmap_state.pop'
file_medium_heatmap_pop_T_2='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T.inp_FeBo__heatmap_occ_2_heatmap_state.pop'
file_medium_heatmap_pop_T_3='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T.inp_FeBo__heatmap_occ_3_heatmap_state.pop'
file_medium_heatmap_pop_T_4='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T.inp_FeBo__heatmap_occ_4_heatmap_state.pop'
file_medium_heatmap_pop_T_5='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T.inp_FeBo__heatmap_occ_5_heatmap_state.pop'
file_medium_heatmap_pop_T_6='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T.inp_FeBo__heatmap_occ_6_heatmap_state.pop'
file_medium_heatmap_pop_T_7='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T.inp_FeBo__heatmap_occ_7_heatmap_state.pop'
file_medium_heatmap_pop_T_8='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T.inp_FeBo__heatmap_occ_8_heatmap_state.pop'
file_medium_heatmap_pop_T_9='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T.inp_FeBo__heatmap_occ_9_heatmap_state.pop'
file_medium_heatmap_pop_T_10='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T.inp_FeBo__heatmap_occ_10_heatmap_state.pop'

file_medium_heatmap_pop_T_array=[]
for i in range(1,11):
    file_medium_heatmap_pop_T_array.append('/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T.inp_FeBo__heatmap_occ_'+str(i)+'_heatmap_state.pop')
# }

# With Environment {
file_medium_heatmap_pop_T_1_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T_env.inp_FeBo__heatmap_occ_1_heatmap_state.pop'
file_medium_heatmap_pop_T_2_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T_env.inp_FeBo__heatmap_occ_2_heatmap_state.pop'
file_medium_heatmap_pop_T_3_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T_env.inp_FeBo__heatmap_occ_3_heatmap_state.pop'
file_medium_heatmap_pop_T_4_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T_env.inp_FeBo__heatmap_occ_4_heatmap_state.pop'
file_medium_heatmap_pop_T_5_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T_env.inp_FeBo__heatmap_occ_5_heatmap_state.pop'
file_medium_heatmap_pop_T_6_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T_env.inp_FeBo__heatmap_occ_6_heatmap_state.pop'
file_medium_heatmap_pop_T_7_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T_env.inp_FeBo__heatmap_occ_7_heatmap_state.pop'
### }


# With Environment no temp {
file_medium_heatmap_pop_1_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_env.inp_FeBo__heatmap_occ_1_heatmap_state.pop'
file_medium_heatmap_pop_2_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_env.inp_FeBo__heatmap_occ_2_heatmap_state.pop'
file_medium_heatmap_pop_3_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_env.inp_FeBo__heatmap_occ_3_heatmap_state.pop'
file_medium_heatmap_pop_4_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_env.inp_FeBo__heatmap_occ_4_heatmap_state.pop'
file_medium_heatmap_pop_5_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_env.inp_FeBo__heatmap_occ_5_heatmap_state.pop'
file_medium_heatmap_pop_6_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_env.inp_FeBo__heatmap_occ_6_heatmap_state.pop'
file_medium_heatmap_pop_7_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_env.inp_FeBo__heatmap_occ_7_heatmap_state.pop'
### }





#}


#### With Enviroment
file_medium_heatmap_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_env.inp_FeBo__heatmap_heatmap.cum'
file_medium_heatmap_T_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T_env.inp_FeBo__heatmap_heatmap.cum'

file_medium_heatmap_T_pos_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T_env.inp_FeBo__heatmap_heatmap.pom'

file_medium_heatmap_pos_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_env.inp_FeBo__heatmap_heatmap.pom'

### Grid
file_medium_prim='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T.inp_FeBo_primary.grid'

file_medium_sec='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_medium/result/inputfile_Paper_job_cvc_medium_NORM_Vb_0.2_ZeroS_T.inp_FeBo_secondary.grid'


# }

#Small {
file_small_heatmap_T='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_small/result/inputfile_Paper_job_cvc_small_small_Vb_0.05_ZeroS_T.inp_FeBo__heatmap_heatmap.cum'

file_small_heatmap_pos_T='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_small/result/inputfile_Paper_job_cvc_small_small_Vb_0.05_ZeroS_T.inp_FeBo__heatmap_heatmap.pom'

file_small_heatmap='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_small/result/inputfile_Paper_job_cvc_small_small_Vb_0.05_ZeroS.inp_FeBo__heatmap_heatmap.cum'

### With Enviroment
file_small_heatmap_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_small/result/inputfile_Paper_job_cvc_small_small_Vb_0.05_ZeroS_env.inp_FeBo__heatmap_heatmap.cum'

file_small_heatmap_T_env='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_small/result/inputfile_Paper_job_cvc_small_small_Vb_0.05_ZeroS_T_env.inp_FeBo__heatmap_heatmap.cum'
### Position
file_small_heatmap_T_env_pos='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_small/result/inputfile_Paper_job_cvc_small_small_Vb_0.05_ZeroS_T_env.inp_FeBo__heatmap_heatmap.pom'

### Grid {
file_small_prim='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_small/result/inputfile_Paper_job_cvc_small_small_Vb_0.05_ZeroS_T.inp_FeBo_primary.grid'

file_small_sec='/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_small/result/inputfile_Paper_job_cvc_small_small_Vb_0.05_ZeroS_T.inp_FeBo_secondary.grid'
### }

#}
