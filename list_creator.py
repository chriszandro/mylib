import math as math

def magnitude_list(magnitude_start=10, magnitude_end=10, splitt_number=9, grid=1000):

    splitt_tupels = []
    index_runner = 0

    for magnitude in range(magnitude_start, magnitude_end + 1):

        start = math.pow(10,magnitude) 
        end  = math.pow(10,magnitude+1) 
        splitt = (end-start)/splitt_number 

        for i in range(1, splitt_number):
            index_runner += 1

            start_point = start + i * splitt
            end_point = start + (i+1) * splitt

            tulpel = {"start":start_point, "end":end_point, "index":index_runner, "grid":grid}
            splitt_tupels.append(tulpel)

    return splitt_tupels

