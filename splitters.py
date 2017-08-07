import numpy as np
import os as os


def create_splitted_files(filename):
    data_matrix = np.loadtxt(filename, usecols=(0, 1, 2, 3))
    # parameter = np.loadtxt(filename, usecols=(0,))
    # position = np.loadtxt(filename, usecols=(1,))
    # current = np.loadtxt(filename, usecols=(2,))
    # energy = np.loadtxt(filename, usecols=(2,))

    print("Files Loaded")
    output_parameter = filename_converter(filename, "parameter")
    output_position = filename_converter(filename, "position")
    output_current = filename_converter(filename, "current")
    output_energy = filename_converter(filename, "energy")

    np.save(output_parameter, data_matrix[:, 0])
    np.save(output_position, data_matrix[:, 1])
    np.save(output_current, data_matrix[:, 2])
    np.save(output_energy, data_matrix[:, 3])

    print("Paramter is saved to:", output_parameter + ".npy")
    print("Position ist saved to:", output_position + ".npy")
    print("Current is saved to:", output_current + ".npy")
    print("Energy is saved to:", output_energy + ".npy")

    return


def filename_converter(filename, specifier):
    return os.path.splitext(filename)[0] + "_SPLITT_" + specifier
