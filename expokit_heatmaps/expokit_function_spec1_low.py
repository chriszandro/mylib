import numpy as np
import list_creator as list_creator
import expokit_heatmap_function as expokit

#Parameter
spec="spec_1_low"
gate_start = 0.0
T=293
en = 0.001
bias = 0.30

#Gate End List Preparation 
gate_points_regular_grid = 300 
gate_points_sub_grid = 15 

## Resonances 
large_resonance_plus = [0.695, 2.0, 3.305,4.61,5.95]
large_resonance_minus = [-3.2, -1.95, -0.61]

## List Creation
gate_end_list =sorted(np.linspace(0, 1.5, gate_points_sub_grid).tolist() +  np.linspace(1.5,7,gate_points_regular_grid).tolist() + list_creator.resonance_refinement(large_resonance_plus, width=0.18, resolution=19))

## Function Call
k = expokit.create_expokit_heatmap(spec=spec, gate_start=gate_start, T=T, en=en, bias=bias, gate_end_list=gate_end_list) 

