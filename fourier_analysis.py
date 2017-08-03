import analysis as analysis
import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack
import analysis as analysis
from matplotlib.colors import LogNorm

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

    :param parameter: Zeitparameter 
    :param variable: Variable for the fourier analysis 
    :return: SampleFrequencies, power 
    """
    # time_vec = parameter * femto2au *au2second

    time_vec = parameter*femto2au
    time_step = np.average(np.diff(time_vec))
    sample_freq = fftpack.fftfreq(len(parameter), d=time_step)
    pidxs = np.where(sample_freq > 0)
    fft = fftpack.fft(variable)
    freqs, power = sample_freq[pidxs], np.abs(fft)[pidxs]
    print("Fourier Analysis is Done")
    return freqs, power
