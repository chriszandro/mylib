# coding: utf-8
from files_large import *
import analysis as analysis
import os

 # No Enviroment { 

 # Current { 
large_heat = analysis.heatmap(heatmap=file_large_heatmap_T, primary_grid=file_large_prim, secondary_grid=file_large_sec, shift = large_symmetric)
medium_heat = analysis.heatmap(heatmap=file_medium_heatmap_T , primary_grid=file_medium_prim, secondary_grid=file_medium_sec, shift = medium_symmetric)
small_heat = analysis.heatmap(heatmap=file_small_heatmap_T, primary_grid=file_small_prim, secondary_grid=file_small_sec, shift = small_symmetric)
 
  # } 

 # Position { 
large_heat_pos = analysis.heatmap(file_large_heatmap_pos_T, primary_grid=file_large_prim, secondary_grid=file_large_sec, shift = large_symmetric)
medium_heat_pos = analysis.heatmap(heatmap=file_medium_heatmap_pos_T, primary_grid=file_medium_prim, secondary_grid=file_medium_sec, shift = medium_symmetric)
small_heat_pos = analysis.heatmap(heatmap=file_small_heatmap_pos_T, primary_grid=file_small_prim, secondary_grid=file_small_sec, shift = small_symmetric)
 
   # } 

# } 

 # With Enviroment { 

 # Current { 
large_heat_env = analysis.heatmap(heatmap=file_large_heatmap_T_env, primary_grid=file_large_prim, secondary_grid=file_large_sec, shift = large_symmetric)
medium_heat_env = analysis.heatmap(heatmap=file_medium_heatmap_T_env , primary_grid=file_medium_prim, secondary_grid=file_medium_sec, shift = medium_symmetric)
small_heat_env = analysis.heatmap(heatmap=file_small_heatmap_T_env, primary_grid=file_small_prim, secondary_grid=file_small_sec, shift = small_symmetric)
 
  # } 

 # Position { 
 
  # } 
large_heat_pos_env = analysis.heatmap(file_large_heatmap_pos_T_env, primary_grid=file_large_prim, secondary_grid=file_large_sec, shift = large_symmetric)
medium_heat_pos_env = analysis.heatmap(heatmap=file_medium_heatmap_pos_T_env, primary_grid=file_medium_prim, secondary_grid=file_medium_sec, shift = medium_symmetric)
small_heat_pos_env = analysis.heatmap(heatmap=file_small_heatmap_pos_T_env, primary_grid=file_small_prim, secondary_grid=file_small_sec, shift = small_symmetric)

  # } 

 # EnergyDiagrams { 

### Energydiagram
medium_thresholds = analysis.energydiagram(energyfile_path=file_medium_dia, shift = medium_symmetric)
### Energydiagram
large_thresholds = analysis.energydiagram(energyfile_path=file_large_dia, shift = large_symmetric)
### Energydiagram
small_thresholds = analysis.energydiagram(energyfile_path=file_small_dia, shift = small_symmetric)
 
  # } 

print ("Heatmap Objects are loaded")
