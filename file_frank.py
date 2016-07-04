# vim: set sw=4 ts=4 sts=4 et tw=78 foldmarker={,} foldlevel=0 foldmethod=marker:

### Insert all franks with 0 here
number_list = range(0,10)
shift_list = [-0.4,-0.2,0,0.2,0.4]

file_frank_0_array = []
for i in number_list:
    print (i)
    file_frank_0_array.append('/home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank0.inp_FeBo__switchmod_bias_at0.000_diagonal_'+ str(i) +'_frank_matrix.frank')

# /home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank-0.2.inp_FeBo__switchmod_bias_at0.000_diagonal_0_frank_matrix.frank
# /home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank0.2.inp_FeBo__switchmod_bias_at0.000_diagonal_0_frank_matrix.frank
# /home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank-0.2.inp_FeBo__switchmod_bias_at0.300_diagonal_0_frank_matrix.frank
# /home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank0.2.inp_FeBo__switchmod_bias_at0.300_diagonal_0_frank_matrix.frank
# /home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank-0.2_no.inp_FeBo__switchmod_bias_at0.000_diagonal_0_frank_matrix.frank
# /home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank0.2_no.inp_FeBo__switchmod_bias_at0.000_diagonal_0_frank_matrix.frank
# /home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank-0.2_no.inp_FeBo__switchmod_bias_at0.300_diagonal_0_frank_matrix.frank
# /home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank0.2_no.inp_FeBo__switchmod_bias_at0.300_diagonal_0_frank_matrix.frank
# /home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank-0.4.inp_FeBo__switchmod_bias_at0.000_diagonal_0_frank_matrix.frank
# /home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank0.4.inp_FeBo__switchmod_bias_at0.000_diagonal_0_frank_matrix.frank
# /home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank-0.4.inp_FeBo__switchmod_bias_at0.300_diagonal_0_frank_matrix.frank
# /home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank0.4.inp_FeBo__switchmod_bias_at0.300_diagonal_0_frank_matrix.frank
# /home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank-0.4_no.inp_FeBo__switchmod_bias_at0.000_diagonal_0_frank_matrix.frank
# /home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank0.4_no.inp_FeBo__switchmod_bias_at0.000_diagonal_0_frank_matrix.frank
# /home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank-0.4_no.inp_FeBo__switchmod_bias_at0.300_diagonal_0_frank_matrix.frank
# /home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank0.4_no.inp_FeBo__switchmod_bias_at0.300_diagonal_0_frank_matrix.frank
# /home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank0.inp_FeBo__switchmod_bias_at0.000_diagonal_0_frank_matrix.frank
# /home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank0.inp_FeBo__switchmod_bias_at0.300_diagonal_0_frank_matrix.frank
# /home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank0_no.inp_FeBo__switchmod_bias_at0.000_diagonal_0_frank_matrix.frank
# /home/vault/mpet/mpet07/projects/paper/switching_frank/inputfile_weak_switching_frank0_no.inp_FeBo__switchmod_bias_at0.300_diagonal_0_frank_matrix.frank

### build an array of them 

# file_small_heatmap_pop_array=[]
# for i in range(1,11):
    # file_small_heatmap_pop_array.append('/home/vault/mpet/mpet07/projects/perfect_heatmaps/Paper_job_cvc_small/result/inputfile_Paper_job_cvc_small_small_Vb_0.05_ZeroS.inp_FeBo__heatmap_occ_' + str(i) + '_heatmap_state.pop')
