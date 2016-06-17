import human_readable as human
import cluster
import numpy as np
import math
import time

large_resonance = [-3.2, -1.9,0.695, 2.0, 3.305,4.61,5.95]
medium_resonance = [-0.41, 1, 2.41]
small_resonance = []

#Fahren um die Resonanzen herum


def time_list(u_start, u_end, liste_resonance, points_u, points_res, resonance_surround):

    delta = abs((u_start - u_end)/(points_u))
    non_resonant = [ u_start + i * delta for i in range(1, points_u)]

    return non_resonant 


erste_liste = time_list(u_start=-3.5, u_end=6, liste_resonance=[0,1], points_u=10, points_res=10, resonance_surround=0.1)


print erste_liste

