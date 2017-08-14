import numpy as np
import os as os

test_pfad = 'D:/data/dynamik_einzeln/24_weak_g0/short'

def load_splitted_files(filename):
    paramter = np.load(os.path.splitext(filename)[0] + "_SPLITT_" + "parameter.npy")
    position = np.load(os.path.splitext(filename)[0] + "_SPLITT_" + "position.npy")
    current = np.load(os.path.splitext(filename)[0] + "_SPLITT_" + "current.npy")
    energy = np.load(os.path.splitext(filename)[0] + "_SPLITT_" + "energy.npy")

    return {"parameter": paramter, "position": position, "current": current, "energy": energy}

def create_splitted_files(filename):
    data_matrix = np.loadtxt(filename, usecols=(0, 1, 2, 3))

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

def create_splitted_population_files(filename):
    data_matrix = np.loadtxt(filename)
    output_population = filename_converter(filename, "POP_0")
    np.save(output_population, data_matrix)
    print("Population is saved to:", output_population+ ".npy")

def splitt_files_in_folder(folder):
    for subdir, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith("evo"):
                print ('Processing file :', file)
                create_splitted_files(os.path.join(subdir, file))


def splitt_population_files_in_folder(folder):
    for subdir, dirs, files in os.walk(folder):
        for file in files:
           if file.endswith("p0"):
               create_splitted_files(os.path.join(subdir, file))


        # normed_path = os.path.normpath(subdir)
        # if (os.path.basename(normed_path)) == "result":
        #     spec = normed_path.split(os.sep)[-2]
        #     print("Processing: ", spec)
        #     os.chdir(subdir)
        #     command = 'cat $(ls -v) > merged_' + spec
        #     subprocess.Popen([command])

def filename_converter(filename, specifier):
    return os.path.splitext(filename)[0] + "_SPLITT_" + specifier


