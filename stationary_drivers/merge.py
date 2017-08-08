import numpy as np
import energy as energy

filename_spec = "D:\data\data_large\G0.0_4.61_B0.3\inputfile_switch_expo_LARGE_G0.0_4.61_Vb_0.8_B_0.3_Switch_ON__ZeroS_T_LARGE_G0.0_4.61_Vb_0.8_B_0.3_Switch_ON__ZeroS_T_"
file_tail = "_.inp_FeBo__exptime.evo"

file_1 = np.loadtxt(filename_spec + "1" + file_tail)
file_2 = np.loadtxt(filename_spec + "2" + file_tail)

file_1[1, 0]
file_1[-1, 0]
file_2[1, 0]
file_2[-1, 0]

cool = np.append(file_1, file_2)

cool[1, 0]

# xargs < filelist cat > final_file.txt
