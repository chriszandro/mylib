# vim: set sw=4 ts=4 sts=4 et tw=78 foldmarker={,} foldlevel=0 foldmethod=marker:
import analysis as analysis

### Insert all franks with 0 here
number_list = range(0,10)
shift_list = [-0.4,-0.2,0,0.2,0.4]

file_frank_0_array = []
file_frank_0_2_array = []
file_frank_m0_2_array = []
file_frank_0_4_array = []
file_frank_m0_4_array = []

for i in number_list:

    path = '/home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank0.inp_FeBo__switchmod_bias_at0.000_diagonal_'+ str(i) +'_frank_matrix.frank'
    file_frank_0_array.append(analysis.frankmatrix(frank_path=path, quanta=i,
        frank_shift=0))

    path = '/home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank-0.2.inp_FeBo__switchmod_bias_at0.000_diagonal_'+ str(i) +'_frank_matrix.frank'
    file_frank_m0_2_array.append(analysis.frankmatrix(frank_path=path,
        quanta=i, frank_shift=-0.2))

    path = '/home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank-0.4.inp_FeBo__switchmod_bias_at0.000_diagonal_'+ str(i) +'_frank_matrix.frank'
    file_frank_m0_4_array.append(analysis.frankmatrix(frank_path=path,
        quanta=i, frank_shift=-0.4))

    path = '/home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank0.2.inp_FeBo__switchmod_bias_at0.000_diagonal_'+ str(i) +'_frank_matrix.frank'
    file_frank_0_2_array.append(analysis.frankmatrix(frank_path=path,
        quanta=i, frank_shift=0.2))

    path = '/home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank0.4.inp_FeBo__switchmod_bias_at0.000_diagonal_'+ str(i) +'_frank_matrix.frank'
    file_frank_0_4_array.append(analysis.frankmatrix(frank_path=path,
        quanta=i, frank_shift=0.4))

