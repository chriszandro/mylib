import numpy as np
import os as os
import scipy.io as sio

def load_splitted_files(filename):

    return


def create_reduced_files(filename):
    data_matrix = np.loadtxt(filename)
    x_grid = np.loadtxt(os.path.splitext(filename)[0] + ".rhot")
    bias_grid = np.loadtxt(os.path.splitext(filename)[0] + ".rhomx")
    output_parameter = filename_converter(filename, "_")
    np.savez_compressed(output_parameter, x=x_grid, y=bias_grid, z=data_matrix)
    print("Matrix is saved to:", output_parameter + ".npz")
    return


def create_reduced_files_mat(filename):
    data_matrix = np.loadtxt(filename)
    x_grid = np.loadtxt(os.path.splitext(filename)[0] + ".rhot")
    bias_grid = np.loadtxt(os.path.splitext(filename)[0] + ".rhomx")
    output_parameter = filename_converter(filename, "_")
    sio.savemat(output_parameter, {'x_grid': x_grid, 'bias_grid':bias_grid, 'data':data_matrix}, do_compression=True)
    print("Matrix saved in Matlab Format to:", output_parameter + ".mat")
    return

def reduce_rhob_files_in_folder(folder):
    for subdir, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith("rhob"):
                print ('Processing file :', file)
                create_reduced_files(os.path.join(subdir, file))
                create_reduced_files_mat(os.path.join(subdir, file))

def filename_converter(filename, specifier):
    return os.path.splitext(filename)[0] + "_REDUCED_" + specifier

testfile = "C:/Users/chriz/Dropbox/PHD/rodeo/mediumdaten/medium/inputfile_cvc_-0_3.inp_FeBo__stat.rhob"
testfolder = "C:/Users/chriz/Dropbox/PHD/rodeo/mediumdaten/medium/"
create_reduced_files(testfolder)

reduce_rhob_files_in_folder(testfolder)

testfile = "C:/Users/chriz/Dropbox/PHD/rodeo/mediumdaten/medium/inputfile_cvc_-0_3.inp_FeBo__stat_REDUCED__.npz"
l = np.load(testfile)


