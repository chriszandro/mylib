# vim: set sw=4 ts=4 sts=4 et tw=78 foldmarker={,} foldlevel=0 foldmethod=marker:
# coding: utf-8

from files_large import *
import analysis as analysis
import os

 # No Enviroment { 

 # Current { 
# # large_heat = analysis.heatmap(heatmap=file_large_heatmap_T, primary_grid=file_large_prim, secondary_grid=file_large_sec, shift = large_symmetric)
# # large_heat_0 = analysis.heatmap(heatmap=file_large_heatmap, primary_grid=file_large_prim, secondary_grid=file_large_sec, shift = large_symmetric)

# medium_heat = analysis.heatmap(heatmap=file_medium_heatmap_T , primary_grid=file_medium_prim, secondary_grid=file_medium_sec, shift = medium_symmetric)
# medium_heat_0 = analysis.heatmap(heatmap=file_medium_heatmap , primary_grid=file_medium_prim, secondary_grid=file_medium_sec, shift = medium_symmetric)

small_heat = analysis.heatmap(heatmap=file_small_heatmap_T, primary_grid=file_small_prim, secondary_grid=file_small_sec, shift = small_symmetric)
small_heat_0 = analysis.heatmap(heatmap=file_small_heatmap, primary_grid=file_small_prim, secondary_grid=file_small_sec, shift = small_symmetric)
 
  # } 

 # Position { 
# large_heat_pos = analysis.heatmap(file_large_heatmap_pos_T, primary_grid=file_large_prim, secondary_grid=file_large_sec, shift = large_symmetric)
# large_heat_pos_0 = analysis.heatmap(file_large_heatmap_pos, primary_grid=file_large_prim, secondary_grid=file_large_sec, shift = large_symmetric)

# medium_heat_pos = analysis.heatmap(heatmap=file_medium_heatmap_pos_T, primary_grid=file_medium_prim, secondary_grid=file_medium_sec, shift = medium_symmetric)
# medium_heat_pos_0 = analysis.heatmap(heatmap=file_medium_heatmap_pos, primary_grid=file_medium_prim, secondary_grid=file_medium_sec, shift = medium_symmetric)

small_heat_pos = analysis.heatmap(heatmap=file_small_heatmap_pos_T, primary_grid=file_small_prim, secondary_grid=file_small_sec, shift = small_symmetric)
small_heat_pos_0 = analysis.heatmap(heatmap=file_small_heatmap_pos, primary_grid=file_small_prim, secondary_grid=file_small_sec, shift = small_symmetric)
 
   # } 

# } 

 # With Enviroment { 

 # env { 

 # Current { 
# large_heat_env = analysis.heatmap(heatmap=file_large_heatmap_T_env, primary_grid=file_large_prim, secondary_grid=file_large_sec, shift = large_symmetric)
# large_heat_env_0 = analysis.heatmap(heatmap=file_large_heatmap_env, primary_grid=file_large_prim, secondary_grid=file_large_sec, shift = large_symmetric)

# medium_heat_env = analysis.heatmap(heatmap=file_medium_heatmap_T_env , primary_grid=file_medium_prim, secondary_grid=file_medium_sec, shift = medium_symmetric)
# medium_heat_env_0 = analysis.heatmap(heatmap=file_medium_heatmap_env , primary_grid=file_medium_prim, secondary_grid=file_medium_sec, shift = medium_symmetric)

small_heat_env = analysis.heatmap(heatmap=file_small_heatmap_T_env, primary_grid=file_small_prim, secondary_grid=file_small_sec, shift = small_symmetric)
small_heat_env_0 = analysis.heatmap(heatmap=file_small_heatmap_env, primary_grid=file_small_prim, secondary_grid=file_small_sec, shift = small_symmetric)
 
  # end current } 

 # Position { 

# large_heat_pos_env = analysis.heatmap(file_large_heatmap_pos_T_env, primary_grid=file_large_prim, secondary_grid=file_large_sec, shift = large_symmetric)
# large_heat_pos_env_0 = analysis.heatmap(file_large_heatmap_pos_env, primary_grid=file_large_prim, secondary_grid=file_large_sec, shift = large_symmetric)

# medium_heat_pos_env = analysis.heatmap(heatmap=file_medium_heatmap_pos_T_env, primary_grid=file_medium_prim, secondary_grid=file_medium_sec, shift = medium_symmetric)
# medium_heat_pos_env_0 = analysis.heatmap(heatmap=file_medium_heatmap_pos_env, primary_grid=file_medium_prim, secondary_grid=file_medium_sec, shift = medium_symmetric)

small_heat_pos_env = analysis.heatmap(heatmap=file_small_heatmap_pos_T_env, primary_grid=file_small_prim, secondary_grid=file_small_sec, shift = small_symmetric)
small_heat_pos_env_0 = analysis.heatmap(heatmap=file_small_heatmap_pos_env, primary_grid=file_small_prim, secondary_grid=file_small_sec, shift = small_symmetric)
  # end position } 
 
  # end env } 

 # MenvM { 

 # Current { 
 
# large_heat_MenvM = analysis.heatmap(heatmap=file_large_heatmap_T_MenvM, primary_grid=file_large_prim, secondary_grid=file_large_sec, shift = large_symmetric)


# medium_heat_MenvM = analysis.heatmap(heatmap=file_medium_heatmap_T_MenvM , primary_grid=file_medium_prim, secondary_grid=file_medium_sec, shift = medium_symmetric)
# medium_heat_MenvM_0 = analysis.heatmap(heatmap=file_medium_heatmap_MenvM , primary_grid=file_medium_prim, secondary_grid=file_medium_sec, shift = medium_symmetric)

small_heat_MenvM = analysis.heatmap(heatmap=file_small_heatmap_T_MenvM, primary_grid=file_small_prim, secondary_grid=file_small_sec, shift = small_symmetric)
small_heat_MenvM_0 = analysis.heatmap(heatmap=file_small_heatmap_MenvM, primary_grid=file_small_prim, secondary_grid=file_small_sec, shift = small_symmetric)
 
 # end current } 

 # Position { 

# large_heat_pos_MenvM = analysis.heatmap(file_large_heatmap_pos_T_MenvM, primary_grid=file_large_prim, secondary_grid=file_large_sec, shift = large_symmetric)

# medium_heat_pos_MenvM = analysis.heatmap(heatmap=file_medium_heatmap_pos_T_MenvM, primary_grid=file_medium_prim, secondary_grid=file_medium_sec, shift = medium_symmetric)

# medium_heat_pos_MenvM = analysis.heatmap(heatmap=file_medium_heatmap_pos_T_MenvM, primary_grid=file_medium_prim, secondary_grid=file_medium_sec, shift = medium_symmetric)

# medium_heat_pos_MenvM_0 = analysis.heatmap(heatmap=file_medium_heatmap_pos_MenvM, primary_grid=file_medium_prim, secondary_grid=file_medium_sec, shift = medium_symmetric)

small_heat_pos_MenvM = analysis.heatmap(heatmap=file_small_heatmap_pos_T_MenvM, primary_grid=file_small_prim, secondary_grid=file_small_sec, shift = small_symmetric)

small_heat_pos_MenvM_0 = analysis.heatmap(heatmap=file_small_heatmap_pos_MenvM, primary_grid=file_small_prim, secondary_grid=file_small_sec, shift = small_symmetric)

  # end position } 

  # end MenvM } 

  # end environment } 

 # EnergyDiagrams { 

### Energydiagram
medium_thresholds = analysis.energydiagram(energyfile_path=file_medium_dia, shift = medium_symmetric)
### Energydiagram
large_thresholds = analysis.energydiagram(energyfile_path=file_large_dia, shift = large_symmetric)
### Energydiagram
small_thresholds = analysis.energydiagram(energyfile_path=file_small_dia, shift = small_symmetric)
 
  # } 

print ("Heatmap Objects are loaded")
