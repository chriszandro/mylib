
import human_readable as human
import cluster
import math
import time
import os
import list_creator as list_creator
import analysis
from shutil import copyfile
from subprocess import call
import numpy as np


gate_points_regular_grid = 601
## Resonances 
large_resonance_plus = [2.0, 1.5]

## List Creation

### Lists
gate_end_list =sorted(np.linspace(1,7,gate_points_regular_grid).tolist() )
        
        #+ list_creator.resonance_refinement(large_resonance_plus, width=0.050, resolution=2))

print gate_end_list

# First Numpy
