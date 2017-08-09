import numpy as np
from scipy import fftpack
import os

au2second = 2.418884254e-17
au2femto = au2second*1e15
femto2au = 1/au2femto
au2ev = 27.21138
ev2au = 1/au2ev
eVtoHz = 2.41798945e14
Hztoau = 4.13413732914335e16
factor = eVtoHz / Hztoau
bohrtoangstrom = 0.529177249

def fourier_transform(parameter, variable):

    """

    :param parameter: zeitparameter 
    :param variable: variable for the fourier analysis 
    :return: samplefrequencies, power 
    """
    # time_vec = parameter * femto2au *au2second

    time_vec = parameter*femto2au
    time_step = np.average(np.diff(time_vec))
    N = len(parameter)
    sample_freq = fftpack.fftfreq(N, d=time_step)
    pidxs = np.where(sample_freq > 0)
    fft = fftpack.fft(variable)
    freqs, power = sample_freq[pidxs], np.abs(fft)[pidxs]
    amplitude = power*(2.0/N)

    print("Fourier Analysis is Done")
    return freqs, amplitude

def create_fourier_files(filename):

    parameter = np.loadtxt(filename, usecols=(0,))
    position = np.loadtxt(filename, usecols=(1,))
    freqs, power = fourier_transform(parameter, position)

    output_freq = filename_converter(filename, "freq" )
    output_pos = filename_converter(filename, "position" )

    np.save(output_pos, power)
    np.save(output_freq, freqs)

    print("Frequencies are saved to:", output_freq + ".npy")
    print("Positions are saved to:", output_pos + ".npy")

    return freqs, power

def filename_converter(filename, specifier):
    return os.path.splitext(filename)[0] + "_FOURIER_" + specifier
<<<<<<< HEAD
=======
>>>>>>> 5588e5bd25dbbd336fe5ea987d31b0ef90fca01c
