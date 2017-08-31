import numpy as np
import matplotlib.pyplot as plt
import list_creator as list_creator

#Parameter
spec="spec_g0_B0"
gate_start = 0.0
T=293
en = 0.000
bias = 0.00

#Gate End List Preparation
gate_points_regular_grid = 550
gate_points_sub_grid = 15

## List Creation
large_resonance_plus = [5.95+1.3, 5.95+2*1.3, 5.95+3*1.3]

gate_end_list=sorted(np.linspace(7, 13, gate_points_regular_grid).tolist() + list_creator.resonance_refinement(large_resonance_plus, width=0.12, resolution=13))
array = np.array(gate_end_list)
print(len(gate_end_list))

fig, ax = plt.subplots(1,1)
ax.plot(((array-2)/1.3), marker=".")
ax.axhline(1)
ax.axhline(2)
ax.axhline(3)
ax.axhline(4)
plt.show()