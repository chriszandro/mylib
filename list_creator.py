def magnitude_list(magnitude_start=10, magnitude_end=10, splitt_number=9, grid=1000):
    
    import math as math

    splitt_tupels = []
    index_runner = 0

    for magnitude in range(magnitude_start, magnitude_end + 1):

        start = math.pow(10,magnitude) 
        end  = math.pow(10,magnitude+1) 
        splitt = (end-start)/splitt_number

        for i in range(0, splitt_number):
            index_runner += 1
            start_point = start + i * splitt
            end_point = start + (i+1) * splitt

            print(i, "%E" % start_point, "%E" % end_point)
            tulpel = {"start":start_point, "end":end_point, "index":index_runner, "grid":grid}
            splitt_tupels.append(tulpel)

    return splitt_tupels

def magnitude_list_frequenzsonden(magnitude_start=9, magnitude_end=10):

    import math as math

    splitt_tupels = []
    index_runner = 0
    grid=1e7 # Maximal Value of the lima machine
    end_point_value = 1e8

    for magnitude in range(magnitude_start, magnitude_end + 1):
        for i in range(0,10):
            index_runner = index_runner + 1
            start = i*math.pow(10, magnitude)
            end = start + end_point_value
            tulpel = {"start":start, "end":end, "index":index_runner, "grid":grid}
            splitt_tupels.append(tulpel)

    return splitt_tupels

def resonance_refinement(reso_list, width=0.1, resolution=11):
    
    import numpy as np

    refinement = []
    liste =  [list(np.linspace(item - width*0.5, item + width*0.5, resolution).tolist()) for item in reso_list]

    for item in liste: 
        refinement = refinement + item

    return refinement

