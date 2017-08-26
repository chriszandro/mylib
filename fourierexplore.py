from scipy import fftpack
import numpy as np

def example_frequency_grid(time_start, time_end, time_grid_length):
    time_step = (time_end - time_start) / time_grid_length
    time_grid = [time_start + (i - 1) * time_step for i in range(0, int(time_grid_length))]
    N = len(time_grid)
    time_step_after = np.average(np.diff(time_grid))
    print(time_step_after)
    sample_freq = fftpack.fftfreq(N, d=time_step_after)
    pidxs = np.where(sample_freq > 0)
    print(time_step_after, "%E" % N)
    factor = 1.0 / (time_step_after * N)
    return sample_freq[pidxs], factor


sample_array, factor = example_frequency_grid(0, 1e7, 1e8)
print(sample_array[0:10], sample_array.shape)
print factor

signal = np.array([-2, 8, 6, 4, 1, 0, 3, 5], dtype=float)
fourier = np.fft.fft(signal)
n = signal.size
timestep = 0.1
freq = np.fft.fftfreq(n, d=timestep)
freq
print n
print 1.0 / (n * 0.1)


# pidxs = np.where(sample_freq > 0)
# fft = fftpack.fft(variable)
# freqs, power = sample_freq[pidxs], np.abs(fft)[pidxs]
# amplitude = power*(2.0/N)
