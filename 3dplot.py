from mayavi import mlab
from files_large  import *
import analysis as analysis

pop_medium_T = [analysis.heatmap(heatmap=file_in, 
                                primary_grid=file_medium_prim, secondary_grid=file_medium_sec) 
             for file_in in file_medium_heatmap_pop_T_array]

test = pop_medium_T[0]