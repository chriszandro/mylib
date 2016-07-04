'''
@author: chriszandro
'''
import os
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


class system(object):
    '''
    @param au2second: cool
    '''

    def __init__(self, computation_data, system_data="None", occupation_data="None", unoccupation_data="None", franck_data="None", prob_data="None"):
        '''
            System
        '''

        self.au2second = 2.4188843e-17 * 1e15
        "cool"

        self.eVtoHz = 2.41798945e14
        self.Hztoau = 4.13413732914335e16
        self.factor = self.eVtoHz / self.Hztoau
        self.bohrtoangstrom = 0.529177249

        # Reading COMPUTATION .dat files
        if computation_data != "None":
            self.computation_data = np.loadtxt(computation_data)

            # Distribution of COMPUTATION Data Sets over numpy arrays
            self.parameter = self.computation_data[:, 0]
            self.position = self.computation_data[:, 1]
            self.current = self.computation_data[:, 2]
            self.energy = self.computation_data[:, 3]
            self.bridge_occupation = self.computation_data[:, 4]
            self.bridge_unoccupation = self.computation_data[:, 5]

        # Reading SYSTEM .sum files
        if system_data != "None":

            self.system_data = np.loadtxt(system_data, comments='?')

            # Distribution of SYSTEM
            self.grid = self.system_data[:, 0]
            self.energy_unoccupied = self.system_data[:, 1]
            self.energy_occupied = self.system_data[:, 2]
            self.potential_unoccupied = self.system_data[:, 3]
            self.potential_occupied = self.system_data[:, 4]
            self.switch = self.system_data[:, 5]
            self.gate = self.system_data[:, 6]
            self.wavefunction = self.system_data[:, 7:]
            self.spectralength = len(self.energy_occupied)
            self.spectra_range = range(0, self.spectralength)
            print ( "Spectral Length: ", self.spectralength)
       
       # READING OCCUPATION .po
        if occupation_data != "None":
                self.occupation = np.loadtxt(occupation_data, unpack=True, comments='?')

                self.occupation_max = np.shape(self.occupation)

        # READING OCCUPATION .p1
        if unoccupation_data != "None":
            self.unoccupation = np.loadtxt(unoccupation_data, unpack=True, comments='?')

        # READING Quasi Franck-Condon Matrix File .cou
        if franck_data != "None":
            self.franck = np.loadtxt(franck_data, comments='?')

        self.exitation_list = [[],[],[]]
        
        # Tunnel Probability
        if prob_data != "None":
            self.prob = np.loadtxt(prob_data, comments='?')
            self.left_tunnel = self.prob[:, 1]
            self.right_tunnel = self.prob[:, 2]


    def integralS(self, axes, plot_number=50):
        lrange = range(1, plot_number)

        SO = [np.sum(self.energy_occupied[i] + ((self.wavefunction[:, i] - self.energy_occupied[i]))) for i in lrange]
        axes.plot(lrange, SO, label='state' + str(i))

        return axes


    # Returns the sum of occupation of given states
    # states: number of states for occupied states
    def occupationsum(self, states):

        summation = np.sum([self.occupation[i + 1] for i in states], axis=0) 
        return summation


    def plot_transition(self, axes, quanta, inverseplot=False):

        transitions, pair, rangel = self.exitation(0, 200, quanta)

        if inverseplot:
            axes.plot(rangel, transitions, 'o--', label='l=' + str(quanta))
            axes.set_ylabel('Threshold Voltage [V]')
            # axes.xaxis.set_ticks_position('top') 

        else:
            axes.plot(transitions, rangel, 'o--', label='l=' + str(quanta))
            axes.set_xlabel('Threshold Voltage [V]')
            # axes.xaxis.set_ticks_position('top') 
        axes.set_ylabel('n')

        return axes

    def plot_transition_dex(self, axes, quanta, inverseplot=False):

        transitions, pair, rangel = self.deexitation(0+quanta, 20, quanta)

        if inverseplot:
            axes.plot(rangel, transitions, 'o--', label='v ' + str(quanta) + '-> m')
            axes.set_ylabel('Voltage [V]')

        else:
            axes.plot(transitions, rangel, 'o--', label='v -> m ' + str(quanta))
            axes.set_xlabel('Voltage [V]')

        axes.set_ylabel('m')

        return axes

    def exitation(self, lower_bound, upper_bound, quanta):

        transition = []
        pair = []

        lrange = range(lower_bound, upper_bound)

        for i in lrange:

            transition.append(2 * (self.energy_occupied[i + quanta] - self.energy_unoccupied[i]))
            pair.append(str(i) + '->' + str(i + quanta))

        return transition, pair, lrange

    def deexitation(self, lower_bound, upper_bound, quanta):

        transition = []
        pair = []

        lrange = range(lower_bound, upper_bound)

        for i in lrange:

            transition_energy = -2 * (self.energy_unoccupied[i+quanta] - self.energy_occupied[i])
            transition.append(transition_energy)

            pair.append(str(i+quanta) + '->' + str(i))

        print (transition_energy, str(i-quanta) + '<-' + str(i))

        return transition, pair, lrange


    def plot_system(self, axes, switch=False, density=False, start=0, end=20, amplification=10):

        axes.plot(self.grid, self.potential_occupied, label='Occupied', color='r', linewidth='2')
        axes.plot(self.grid, self.potential_unoccupied, label='Unoccupied', color='b', linewidth='2')

        if switch:
            axes.plot(self.grid, self.switch, linewidth=2, label='switch', linestyle='-', color='g')

        for i in range(start, end):

            if i % 2 == 0:
                lw = '-'
            else:
                lw = '--'

            if density:
                axes.plot(self.grid, self.energy_occupied[i] + ((self.wavefunction[:, i] - self.energy_occupied[i]) ** 2) * amplification, linewidth=1, linestyle=lw, label='State ' + str(i))
            else:
                axes.plot(self.grid, self.energy_occupied[i] + (self.wavefunction[:, i] - self.energy_occupied[i])*amplification , linewidth=1, linestyle=lw, label='State ' + str(i))

        axes.set_xlabel('Position [a.u.]')
        axes.set_ylabel('Energy [eV]')

        return axes

    def plot_simple_system(self, axes, plotlabel='', switch=False, density=False, start=0, end=20, amplification=10):

        axes.plot(self.grid, self.potential_unoccupied, label=plotlabel, color='r', linewidth='2')

        axes.set_xlabel('Position [a.u.]')
        axes.set_ylabel('Energy [eV]')

        return axes

    def plot_termscheme(self, axes, arrowlist, y0=0, delta_y=0.1, distance=1, cap=10, inputcolor='b'):

        axes.plot(self.grid, self.potential_occupied + distance, label='Occupied', color='r', linewidth='2')
        axes.plot(self.grid, self.potential_unoccupied, label='Unoccupied', color='b', linewidth='2')

        [axes.axhline(_volt, color='b', linewidth=1) for _volt in self.energy_unoccupied[0:cap]]
        [axes.axhline(_volt, color='r', linewidth=1) for _volt in self.energy_occupied + distance]

        for element in arrowlist:
            print (element[0], element[1])

            increment = (self.energy_occupied[element[1]] + distance) - self.energy_unoccupied[element[0]]

            axes.arrow(y0, self.energy_unoccupied[element[0]], 0, self.energy_unoccupied[element[0]] + increment, head_width=0.05, fc="k", ec="k", width=0.02, head_length=0.02, length_includes_head=True, color=inputcolor)
            y0 = y0 + 0.2

        axes.set_yticklabels([])
        axes.set_xlabel('Position [a.u.]')
        axes.set_ylabel('Energy [eV]')

        return axes


    def plot_multi(self):

        f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

        ax1.plot(self.parameter, self.current, label='Current', color='r')
        ax2.plot(self.parameter, self.position, label='Position', color='b')
        ax3.plot(self.parameter, self.energy, label='Energie', color='b')
        ax4.plot(self.parameter, self.bridge_occupation, label='Occupation')

        return f

    def franckmatrix(self, f, axes, vminInput=0, vmaxInput=1):
        cax = axes.matshow(np.log10(self.franck), interpolation='nearest', vmin=vminInput, vmax=vmaxInput)

        axes.set_title('$\log_{10}{|<0,n|s(x)|v,1>|^2}$', y=1.08)
        axes.set_xlabel('n')
        axes.set_ylabel('v')
        f.colorbar(cax)
        return cax

    def plot_current(self, axes , scale='lin', name=''):

        axes.set_xscale(scale)
        axes.plot(self.parameter, self.current, linestyle='-', lw='2', label=name)

        # ax.set_xlabel('Voltage [V]')
        axes.set_ylabel('Current [$\mu$ A]')
        # axes.set_ylabel('Current nA')

        return axes

    def plot_position(self, axes , siunits=False, scale='lin', name=''):


        if siunits:
            axes.plot(self.parameter, self.position, linestyle='-', lw='2', label=name)
            axes.set_xscale(scale)
            axes.set_xlabel('Voltage [V]')
            # ax.set_ylabel('Current [$\mu$ A]')
            axes.set_ylabel('Position [a.u]')
        else:
            axes.plot(self.parameter, self.position * self.bohrtoangstromtoangstrom, linestyle='-', lw='2', label=name)
            axes.set_xscale(scale)
            axes.set_xlabel('Voltage [V]')
            # ax.set_ylabel('Current [$\mu$ A]')
            axes.set_ylabel('Position [a.u]')


        return axes

    def plot_current_t(self, axes , scale='lin', style='-', colorp="b", name='', siunits=True):

        axes.set_xscale(scale)

        if siunits:
            axes.plot(self.parameter, self.current, linestyle=style, color=colorp, lw='2', label=name)
            # ax.set_xlabel('Time [a.u.]')
            axes.set_ylabel('Current [$\mu$A]')
        else:
            axes.plot(self.parameter * self.au2second, self.current, color=colorp, linestyle=style, lw='2', label=name)
            # ax.set_xlabel('Seconds')
            axes.set_ylabel('Current [$\mu$A]')
        return axes

    def plot_position_t(self, axes , scale='lin', style='-', colorp="b", siunits=True, name=''):

        axes.set_xscale(scale)

        if siunits:
            axes.plot(self.parameter, self.position, linestyle=style, lw='2', color=colorp, label=name)
            axes.set_xlabel('Time [a.u]')
            axes.set_ylabel('Position [a.u]')
        else:
            axes.plot(self.parameter * self.au2second, self.position * self.bohrtoangstrom, linestyle=style, color=colorp, lw='2', label=name)
            axes.set_xlabel('Time [fs]')
            axes.set_ylabel('Position [$\AA$]')
        return axes

    def plot_energy_t(self, axes , style='-', scale='lin', colorp="b",  siunits=True, name=''):

        axes.set_xscale(scale)

        if siunits:
            axes.plot(self.parameter, self.energy, linestyle=style, lw='2', color=colorp, label=name)
            axes.set_xlabel('Time [a.u]')
            axes.set_ylabel('Energy [eV]')
        else:
            axes.plot(self.parameter * self.au2second, self.energy, linestyle=style, color=colorp, lw='2', label=name)
            axes.set_xlabel('Time [fs]')
            axes.set_ylabel('Energy [eV]')
        return axes

    def plot_population(self, axes, pop_number=10, scale='lin', name=''):

        axes.set_xscale(scale)
        axes.set_xlabel('Time [fs]')
        axes.set_ylabel('Population')

        axes.set_title(name)

        for i in range(1, pop_number):

            axes.plot(self.occupation[0] * self.au2second, self.occupation[i], linestyle='-', lw='2', label='State' + str(i - 1))
        return axes

    def plot_notpopulation(self, axes, pop_number=10, scale='lin'):

        axes.set_xscale(scale)
        axes.set_xlabel('Voltage [V]')
        axes.set_ylabel('Not Population')

        for i in range(1, pop_number):

            axes.plot(self.unoccupation[0], self.unoccupation[i], linestyle='-', lw='2', label='State' + str(i - 1))

        return axes

    def putexitationlines(self, axes, quanta=1, start=0, end=20):

        exitations, pair, lrange = self.exitation(start, end, quanta)
        axes.xaxis.set_ticks_position('top') 
        [axes.axvline(_volt, linewidth=1) for _volt in exitations]

        axes.set_xticks(exitations)
        axes.set_xticklabels(pair , fontsize=7)


        return axes


    def putdeexitationlines(self, axes, quanta=1, start=0, end=20):

        deexitations, pair, lrange = self.deexitation(start, end, quanta)

        [axes.axvline(_volt, linewidth=1) for _volt in deexitations]

        axes.set_xticks(deexitations)
        axes.set_xticklabels(pair , fontsize=7)

        return axes


    def putdeexitationslist(self, axes, exlist, inputcolor='b'):

        transition = []
        pair = []

        # Caclulate
        for element in exlist:
            transition.append(2 * (self.energy_occupied[element[1]] - self.energy_unoccupied[element[0]]))
            pair.append(str(element[0]) + '>' + str(element[1]))

        # Put into List
        [axes.axvline(_volt, linewidth=2, color=inputcolor) for _volt in transition]

        axes.set_xticks(transition)
        axes.set_xticklabels(pair , color=inputcolor, fontsize=7)

        return axes

    def putexitationslist(self, axes, exlist, inputcolor='b'):

        transition = []
        pair = []

        # Caclulate
        for element in exlist:
            transition.append(2 * (self.energy_occupied[element[1]] - self.energy_unoccupied[element[0]]))
            pair.append(str(element[0]) + '>' + str(element[1]))


        # Put into List
        [axes.axvline(_volt, linewidth=2, color=inputcolor) for _volt in transition]

        axes.set_xticks(transition)
        axes.set_xticklabels(pair , color=inputcolor, fontsize=7)

        return axes

    # Attention: Method works only for grid with a unit stepsize
    def derivate_energy(self):

        stepsize = np.average(np.diff(self.parameter))

        # New Grid which is shifted by the half stepsize
        # First temporary Calculation which has one extra grid ponts
        new_grid_temp = self.parameter + stepsize / 2
        # Real grid which excludes the last item
        new_grid = new_grid_temp[0:-1]

        # Calc Differences between values
        d_energy = np.diff(self.energy) / stepsize

        return (d_energy, new_grid)

    def plot_energy_derivate_t(self, axes , style='-', scale='lin', colorp="b",  siunits=True, name=''):

        axes.set_xscale(scale)

        d_energy, grid = self.derivate_energy()

        if siunits:
            axes.plot(grid, d_energy, linestyle=style, lw='2', color=colorp, label=name)
            axes.set_xlabel('Time [a.u]')
            axes.set_ylabel('dE/dt [a.u.]')
        else:
            axes.plot(grid * self.au2second, d_energy, linestyle=style, color=colorp, lw='2', label=name)
            axes.set_xlabel('Time [fs]')
            axes.set_ylabel('dE/dt [eV/s]')
        return axes
# Attention: Method works only for grid with a unit stepsize
    def derivate_position(self):

        stepsize = np.average(np.diff(self.parameter))

        # New Grid which is shifted by the half stepsize
        # First temporary Calculation which has one extra grid ponts
        new_grid_temp = self.parameter + stepsize / 2
        # Real grid which excludes the last item
        new_grid = new_grid_temp[0:-1]

        # Calc Differences between values
        d_position = np.diff(self.position) / stepsize

        return (d_position, new_grid)

    def derivate_current(self):

        stepsize = np.average(np.diff(self.parameter))

        # New Grid which is shifted by the half stepsize
        # First temporary Calculation which has one extra grid ponts
        new_grid_temp = self.parameter + stepsize / 2
        # Real grid which excludes the last item
        new_grid = new_grid_temp[0:-1]

        # Calc Differences between values
        d_current = np.diff(self.current) / stepsize

        return (d_current, new_grid)

    def derivate_2_energy(self):

        d_energy, d_grid = self.derivate_energy()

        stepsize = np.average(np.diff(d_grid))
        _
        # New Grid which is shifted by the half stepsize
        # First temporary Calculation which has one extra grid ponts
        new_grid_temp = d_grid + stepsize / 2
        # Real grid which excludes the last item
        new_grid = new_grid_temp[0:-1]

        # Calc Differences between values
        dd_energy = np.diff(d_energy) / stepsize

        return (dd_energy, new_grid)

    def fft_energy(self, axes, colorp='b', name=""):

        time_step = np.average(np.diff(self.parameter))

        sample_freq = fftpack.fftfreq(len(self.energy), d=time_step)

        energy_fft= fftpack.fft(self.energy)
        pidxs = np.where(sample_freq > 0)
        freqs, power = sample_freq[pidxs], np.abs(energy_fft)[pidxs]
        freq = freqs[power.argmax()]

        axes.plot(freqs, power, lw='3', color=colorp, label=name)
        axes.set_xlabel('Frequency [$\omega_0$]')
        axes.set_ylabel('Amplitude')

        return axes

    def fft_energy_derivate(self, axes, colorp='b', name=""):

        d_energy, grid = self.derivate_energy()

        time_step = np.average(np.diff(grid))

        sample_freq = fftpack.fftfreq(len(d_energy), d=time_step)

        energy_fft= fftpack.fft(d_energy)
        pidxs = np.where(sample_freq > 0)
        freqs, power = sample_freq[pidxs], np.abs(energy_fft)[pidxs]
        freq = freqs[power.argmax()]

        axes.plot(freqs, power, lw='3', color=colorp, label=name)
        axes.set_xlabel('Frequency [$\omega_0$]')
        axes.set_ylabel('Amplitude')

        return axes

    def fft_position(self, axes, style='-', colorp='b', name=""):

        time_step = np.average(np.diff(self.parameter))

        sample_freq = fftpack.fftfreq(len(self.position), d=time_step)

        position_fft = fftpack.fft(self.position)
        pidxs = np.where(sample_freq > 0)
        freqs, power = sample_freq[pidxs], np.abs(position_fft)[pidxs]
        freq = freqs[power.argmax()]

        axes.plot(freqs, power, lw='3', linestyle=style, color=colorp, label=name)
        axes.set_xlabel('Frequency [$\omega_0$]')
        axes.set_ylabel('Amplitude')

        return axes

    def fft_current(self, axes):

        time_step = np.average(np.diff(self.parameter))

        sample_freq = fftpack.fftfreq(len(self.current), d=time_step)

        current_fft = fftpack.fft(self.position)
        pidxs = np.where(sample_freq > 0)
        freqs, power = sample_freq[pidxs], np.abs(current_fft)[pidxs]
        freq = freqs[power.argmax()]

        axes.plot(freqs, power, lw='3', color='r')
        axes.set_xlabel('Frequency [$\omega_0$]')
        axes.set_ylabel('Amplitude')

        return axes

    def fft_energy(self, axes):

        time_step = np.average(np.diff(self.parameter))

        sample_freq = fftpack.fftfreq(len(self.energy), d=time_step)

        energy_fft = fftpack.fft(self.energy)
        pidxs = np.where(sample_freq > 0)
        freqs, power = sample_freq[pidxs], np.abs(energy_fft)[pidxs]
        freq = freqs[power.argmax()]

        axes.plot(freqs, power, lw='3', color='r')
        axes.set_xlabel('Frequency [$\omega_0$]')
        axes.set_ylabel('Amplitude')

        return axes


    def putexitationlines_fft(self, axes, fontsizep=7 , quanta=1, start=0, end=20, colorp='b'):

        exitations, pair, lrange = self.exitation_fft(start, end, quanta)

        [axes.axvline(_volt, linewidth=1, color=colorp) for _volt in exitations]

        axes.set_xticks(exitations)
        axes.set_xticklabels(pair , fontsize=fontsizep)


        return axes

    def exitation_fft2(self, color = 'b', lower_bound=0, upper_bound=10, quanta=1):

        transition = []
        pair = []

        lrange = range(lower_bound, upper_bound)

        for i in lrange:

            transition = (self.energy_occupied[i + quanta] - self.energy_occupied[i]) * self.factor
            ticks = str(i) + '->' + str(i + quanta)

            self.exitations.append([transition, ticks, color])

        return

    def exitation_fft(self, lower_bound=0, upper_bound=10, quanta=1):

        transition = []
        pair = []

        lrange = range(lower_bound, upper_bound)

        for i in lrange:

            transition.append((self.energy_occupied[i + quanta] - self.energy_occupied[i]) * self.factor)
            pair.append(str(i) + '->' + str(i + quanta))

        return transition, pair, lrange

    def put_excitation_list(self, axes, fontsize='10'):

        for element in self.exitation_list[2]:
            axes.axvline(element[0], linewidth=1, color=element[1])

        axes.set_xticks(self.exitation_list[0])
        axes.set_xticklabels(self.exitation_list[1] , fontsize=fontsize)

        return axes

    def create_excitation_list(self, lower_bound=0, upper_bound=10, quanta=1, color='b'):


        for i in range(lower_bound, upper_bound):

            self.add_excitations(i, quanta, color)

        pass

    def add_excitations(self, index=1, quanta='1', color='k'):

        transition = (self.energy_occupied[index + quanta] - self.energy_occupied[index]) * self.factor
        label = str(index) + '->' + str(index + quanta)

        self.exitation_list[0].append(transition)
        self.exitation_list[1].append(label)
        self.exitation_list[2].append([transition,color])

        pass


    def scheme_3d(self):

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
       
        transitions, pair, rangel = self.exitation(0, 200, quanta)

        x = transitions
        y = rangel
    
        ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)

        ax.set_zlabel('Z')
        ax.set_xlabel('Voltages [V]')
        ax.set_ylabel('m')

        pass
    
    
    def set_pupblication_style(self):
        rcParams['axes.titlesize'] = 26
        rcParams['axes.labelsize'] = 30
        rcParams['legend.fontsize'] = 26
        rcParams['savefig.dpi'] = 1200
        rcParams['axes.linewidth'] = 2.5

        rcParams['ytick.labelsize'] = 24
        rcParams['ytick.major.pad'] = 12
        rcParams['ytick.major.size'] = 10
        rcParams['ytick.minor.size'] = 8
        rcParams['ytick.major.width'] = 2.5
        rcParams['ytick.minor.width'] = 3

        rcParams['xtick.labelsize'] = 24
        rcParams['xtick.major.pad'] = 12
        rcParams['xtick.major.size'] = 10
        rcParams['xtick.minor.size'] = 8
        rcParams['xtick.major.width'] = 2.5
        rcParams['xtick.minor.width'] = 3

        rcParams['mathtext.fontset'] = 'stixsans'
        rcParams['mathtext.default'] = 'regular'

        rcParams['lines.markersize'] = 14

class density(object):
    def __init__(self, rhoxfile="None", parameter_grid="None", position_grid="None"):
        """
        rhoxfile: File containing the z data
        paramter_grid: Parameter
        position_grid: Position
        """

        if rhoxfile != "None":
            self.data = np.loadtxt(rhoxfile, comments="?")
        if parameter_grid != "None":
            self.parameter_grid = np.loadtxt(parameter_grid)
        if position_grid != "None":
            self.grid = np.loadtxt(position_grid)

        self.number = len(self.data[:, 1])

        # Assign parameter value into single array entries in self.density
        self.density = [self.data[i, :] for i in range(0, self.number)]

        # Coordinate Sytem for plotting
        self.xv, self.yv = np.meshgrid(self.grid, self.parameter_grid)
        self.zv = self.density

    def norm(self):
        integral = [np.trapz(self.density[i], self.grid) for i in range(0, self.number)]
        return integral

    def plotnorm(self, ax):
        normtable = self.norm()
        ax.plot(range(0, self.number), normtable)
        return ax
    def plotdensity(self, ax, index=0, colorb="b", labelb="no label", linestyleb="-"):
        ax.plot(self.grid, self.density[index] , color=colorb, label=labelb, linestyle=linestyleb, linewidth=1.5)
        return ax
    def plotdensity_sgn(self, ax, index=0, colorb="b", labelb="no label", linestyleb="-"):
        ax.plot(self.grid, np.sign(self.density[index]), color=colorb, label=labelb, linestyle=linestyleb, linewidth=1.5)
        return ax
    def signummatrix(self):
        sgnmatrix = [np.sign(initial.densitymatrix[i]) for  i in range(0, initial.number)]
        return sgnmatrix

class energydiagram(object):
    def __init__(self, energyfile_path="None", occupation_energy = 0.1, shift=0):
        if energyfile_path != "None":
            self.energy_dia = np.loadtxt(energyfile_path).T
            
        self.gate_voltages = self.energy_dia[0] - shift   
        self.energys = self.energy_dia[1:]
        
        self.number_of_states = self.energys.shape[0]
        self.number_of_gate_points = self.energys.shape[1]
        self.occupation_energy = occupation_energy

        self.thresholds = self.get_transition_matrix()
        
    def get_transition_matrix(self):
        
        threshold_list = []
        for quanta in range(0, self.number_of_states):
            threshold_list.append(self.get_transition_for_quanta(quanta))
        return threshold_list


    def put_single_transition(self, ax, initial_state=0, end_state=0, lw=2, ls='--', col='b'):
       
        #label_dummy = str(initial_state) + " > "+ str(end_state)
        indecies = str(initial_state+1) + str(end_state+1) 
        label_dummy = "$U_{" + indecies + "}$"

        transition = 2*(self.energys[end_state] + self.occupation_energy - self.energys[initial_state])
        ax.plot(self.gate_voltages, transition, label=label_dummy, linewidth=lw, linestyle=ls, color=col)

        return ax
    
    def put_distance(self, ax, initial_state=0, end_state=0, *args):

        distance = self.energys[end_state] - self.energys[initial_state]
        ax.plot(self.gate_voltages, distance, *args)

        return ax

    def put_transition(self, ax, quanta, end_state=None):    
        
        if end_state is None:
            end_state = (self.number_of_states - quanta)
        
        for i in range(0, end_state):
            ax.plot(self.gate_voltages, self.thresholds[quanta]["threshold"][i], 
                label = str(self.thresholds[quanta]["pair"][i][0]) +" > " + str(self.thresholds[quanta]["pair"][i][1]) )
        
        return ax
            
    def put_transition_const_state(self, ax, state):
        
        for i in range(0, self.number_of_states-state):
            transition = 2*(self.energys[state + i] + self.occupation_energy - self.energys[state])
            ax.plot(self.gate_voltages, transition, label=str(state) + " > "+ str(state + i))
                  
        return ax
        
        
    def get_transition_for_quanta(self, quanta):
        
        transition = []
        pair = []
       
        for i in range(0, (self.number_of_states - quanta)):
        
            transition.append(2*(self.energys[i + quanta] + self.occupation_energy - self.energys[i]))
            pair.append([i, i + quanta])
                  
        return {"pair":pair, "threshold":transition}
        

class heatmap(object):
    def __init__(self, heatmap="None", primary_grid="None", secondary_grid="None", shift=0):
        """
        heatmap: File containing the z data
        primary_grid: The primary grid
        secondar_grid: The secondary grid
        """

        if heatmap != "None":
            self.data = np.loadtxt(heatmap, comments="?")
        if primary_grid != "None":
            self.primary_grid = np.loadtxt(primary_grid)# Bias Voltage, y - axis
        if secondary_grid != "None":
            self.secondary_grid = np.loadtxt(secondary_grid) - shift # Gate Voltage, x - Axis


        #Derivates
        self.primary_diff = np.diff(self.primary_grid)
        #Midpoints for derivates
        self.xd = (self.primary_grid[1:]+ self.primary_grid[:-1])/2

        #Differential Conductance
        self.conductance= None

        self.number = len(self.data[:, 1])


        # Meshgrid for 3d Plots
        self.xv, self.yv = np.meshgrid(self.primary_grid, self.secondary_grid)
        

    def calculate_derivate(self):

        conductance = np.array([np.diff(line) / self.primary_diff  for line in self.data.T]).T

        return conductance

    def plot_data_vs_bias(self, axes , index=1):

        axes.plot(self.primary_grid, self.data[:,index] ,linestyle='-', lw='2', label=str(index) )

        axes.set_xlabel('Bias Voltage [V]')
        axes.set_ylabel('Current [$\mu$ A]')

        return axes
    
    def plot_derivate_data_vs_bias(self, axes , index=1):

        axes.plot(self.xd, self.conductance[:,index] ,linestyle='-', lw='2', label=str(index) )

        axes.set_xlabel('Bias Voltage [V]')
        axes.set_ylabel('Current [$\mu$ A]')

        return axes

    def plot_data_vs_gate(self, axes , index=1):

        axes.plot(self.secondary_grid, self.data[index,:],linestyle='-', lw='2', label=str(index))

        axes.set_xlabel('Gate Voltage [V]')
        axes.set_ylabel('Current [$\mu$ A]')

        return axes


class rhox(object):
    def __init__(self, data="None", primary_grid="None", secondary_grid="None"):
        """
        heatmap: File containing the z data
        paramter_grid: Parameter
        position_grid: Position
        """

        if heatmap != "None":
            self.data = np.loadtxt(data, comments="?")
            self.name = os.path.basename(data)
        if primary_grid != "None":
            self.primary_grid = np.loadtxt(primary_grid)
        if secondary_grid != "None":
            self.secondary_grid = np.loadtxt(secondary_grid)

        # Meshgrid for 3d Plots
        self.xv, self.yv = np.meshgrid(self.secondary_grid, self.primary_grid)

        self.number = len(self.data[:, 1])
        # Assign parameter value into single array entries in self.density
        self.density = [self.data[i, :] for i in range(0, self.number)]

    def plot_overview(self, accuracy=1, save_path="./" ):

        fig = plt.figure(figsize=(24, 12))
        fig.suptitle('Wavepacket overview of ' + self.name, fontsize='17')

        #---- 1. subplot
        ax = fig.add_subplot(2, 2, 1, projection='3d')

        surf1 = ax.plot_surface(self.xv, self.yv, self.data, rstride=accuracy, cstride=accuracy, cmap = cm.jet,
        linewidth=0, antialiased=True)

        ax.view_init(azim=0, elev=45)
        ax.set_xlabel('Position [$\AA$]', fontsize='12')
        ax.tick_params(labelsize='12', length=1, width=1)
        ax.set_ylabel('Time [fs]', fontsize='12')
      #  ax.yaxis.set_scale('log')

        #---- 2. subplot
        ax = fig.add_subplot(2, 2, 2, projection='3d')

        surf2 = ax.plot_surface(self.yv, self.xv, self.data,  rstride=accuracy, cstride=accuracy, cmap = cm.jet,
        linewidth=0, antialiased=True)
        ax.view_init(azim=90, elev=90)
        ax.set_xlabel('Position [a.u.]', fontsize='12')
        ax.tick_params(labelsize='8', length=1, width=1)
        ax.set_ylabel('Time [fs]', fontsize='12')

        #---- 3. subplot
        ax = fig.add_subplot(2, 2, 3, projection='3d')

        surf3 = ax.plot_surface(self.xv, self.yv, self.data,  rstride=accuracy, cstride=accuracy, cmap = cm.jet,
        linewidth=0, antialiased=True)
        ax.set_xlabel('Position [a.u.]', fontsize='12')
        ax.tick_params(labelsize='8', length=1, width=1)
        ax.set_ylabel('Time [fs]', fontsize='12')

        #---- 4. subplot
        ax = fig.add_subplot(2, 2, 4, projection='3d')
        surf4 = ax.plot_surface(self.xv, self.yv, self.data,  rstride=accuracy, cstride=accuracy, cmap = cm.jet,
        linewidth=0, antialiased=True)

        ax.view_init(azim=-69, elev=40)
        ax.set_xlabel('Position [a.u.]', fontsize='12')
        ax.tick_params(labelsize='8', length=1, width=1)
        ax.set_ylabel('Time [fs]', fontsize='12')

        file_name = save_path + self.name + "rhox_overview.png"
        fig.savefig(file_name)



