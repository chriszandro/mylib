'''

@package analysis
Created on Jan 15, 2015

@author: chriszandro
'''

from numpy import *
import numpy as np
    
from pylab import *
    
from scipy import fftpack 
from scipy import constants
from scipy.signal import argrelextrema
from scipy import signal
    
from os.path import expanduser
from mpl_toolkits.mplot3d import Axes3D
    
from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.image as mpimg
from matplotlib import rcParams



class system(object):
   
    '''
    @param au2second: cool
    '''


    def __init__(self, computation_data, system_data="None", occupation_data="None", unoccupation_data="None", franck_data="None"):
        '''
            System
        '''

        self.au2second = 2.4188843e-17*1e15 
        "cool"
        
        self.eVtoHz = 2.41798945e14
        self.Hztoau = 4.13413732914335e16
        self.factor = self.eVtoHz/self.Hztoau
        self.bohrtoangstrom = 0.529177249
        
        #Reading COMPUTATION .dat files
        self.computation_data = np.loadtxt(computation_data)
        
        #Distribution of COMPUTATION
        self.parameter = self.computation_data[:,0]
        self.position = self.computation_data[:,1]
        self.current = self.computation_data[:,2]
        self.energy = self.computation_data[:,3]
        self.bridge_occupation = self.computation_data[:,4]
        self.bridge_unoccupation = self.computation_data[:,5]
        
        #Reading SYSTEM .sum files
        if system_data!="None":
        
            self.system_data = np.loadtxt(system_data, comments='?')
        
            #Distribution of SYSTEM
            self.grid = self.system_data[:,0]
            self.energy_unoccupied = self.system_data[:,1]
            self.energy_occupied = self.system_data[:,2]
            self.potential_unoccupied = self.system_data[:,3]
            self.potential_occupied = self.system_data[:,4]
            self.switch = self.system_data[:,5]
            self.gate = self.system_data[:,6]
            self.wavefunction = self.system_data[:,7:]
            self.spectralength = len(self.energy_occupied)
            self.spectra_range = range(0, self.spectralength)     
        #READING OCCUPATION .po
        if occupation_data!="None":
                self.occupation = np.loadtxt(occupation_data, unpack=True, comments='?')
                
                self.occupation_max = np.shape(self.occupation)
                
        #READING OCCUPATION .p1
        if unoccupation_data!="None":
            self.unoccupation = np.loadtxt(unoccupation_data, unpack=True, comments='?')
        
        #READING Quasi Franck-Condon Matrix File .cou
        if franck_data!="None":
            self.franck = np.loadtxt(franck_data, comments='?')
        
        

    def integralS(self, axes, plot_number=50):
        
        lrange = range(1,plot_number)
        
        SO = [np.sum(self.energy_occupied[i]+((self.wavefunction[:,i]-self.energy_occupied[i]))) for i in lrange] 
        axes.plot(lrange, SO, label = 'state' + str(i))
        
        return axes
        
    
    #Returns the sum of occupation of given states
    #states: number of states for occupied states
    def occupationsum(self, states):
    
        summation = np.sum([self.occupation[i+1] for i in states], axis=0)
        
        return summation
    
        
    def plot_transition(self, axes, quanta, inverseplot=False):
    
        transitions, pair, rangel = self.exitation(0, 200, quanta)
    
        if inverseplot:
            axes.plot(rangel, transitions, 'o--', label='m -> v = m + ' + str(quanta))
            axes.set_ylabel('Voltage [V]')
            
        else:
            axes.plot(transitions, rangel, 'o--', label='m -> v = m + ' + str(quanta))
            axes.set_xlabel('Voltage [V]')
            
        axes.set_ylabel('m')
            
        return axes
 
    
    def exitation(self, lower_bound, upper_bound, quanta):
   
        transition = []
        pair=[]
   
        lrange = range(lower_bound, upper_bound)
        
        for i in lrange:
        
            transition.append(2*(self.energy_occupied[i+quanta]-self.energy_unoccupied[i]))
            pair.append(str(i) + '->' + str(i+quanta))

        return transition, pair, lrange 
    
    
        
    def plot_system(self, axes, switch=False, density=False, start=0, end=20, amplification=10):
             
        axes.plot(self.grid, self.potential_occupied, label='Occupied', color='r', linewidth='2')
        axes.plot(self.grid, self.potential_unoccupied, label='Unoccupied', color='b', linewidth='2')
        
        if switch:
            axes.plot(self.grid, self.switch, linewidth=2, label='switch', linestyle='-', color ='g') 
    
        for i in range(start, end):
            
            if i % 2 == 0: 
                lw = '-'
            else:
                lw = '--'
            
            if density:
                axes.plot(self.grid, self.energy_occupied[i]+((self.wavefunction[:,i]-self.energy_occupied[i])**2)*amplification, linewidth=1, linestyle=lw, label='State ' + str(i)) 
            else:
                axes.plot(self.grid, self.wavefunction[:,i], linewidth=1, linestyle=lw, label='State ' + str(i)) 
                
        axes.set_xlabel('Position [a.u.]')
        axes.set_ylabel('Energy [eV]')
  
        return axes
    
    def plot_simple_system(self, axes, plotlabel='', switch=False, density=False, start=0, end=20, amplification=10):
              
        axes.plot(self.grid, self.potential_unoccupied, label=plotlabel, color='r', linewidth='2')      

        axes.set_xlabel('Position [a.u.]')
        axes.set_ylabel('Energy [eV]')
  
        return axes
    
    def plot_termscheme(self, axes, arrowlist, y0=0, delta_y=0.1, distance = 1, cap=10, inputcolor='b'):
        
        axes.plot(self.grid, self.potential_occupied  + distance, label='Occupied', color='r', linewidth='2')
        axes.plot(self.grid, self.potential_unoccupied, label='Unoccupied', color='b', linewidth='2')
    
        [axes.axhline(_volt, color='b', linewidth=1) for _volt in self.energy_unoccupied[0:cap]]
        [axes.axhline(_volt, color='r', linewidth=1) for _volt in self.energy_occupied+distance]

        for element in arrowlist: 
            print element[0], element[1]
            
            increment =  (self.energy_occupied[element[1]]+distance) - self.energy_unoccupied[element[0]] 
            
            axes.arrow(y0, self.energy_unoccupied[element[0]], 0,self.energy_unoccupied[element[0]] + increment, head_width=0.05,fc="k", ec="k", width = 0.02, head_length=0.02, length_includes_head = True, color = inputcolor)
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
        ax4.plot(self.parameter, self.bridge_occupation, label='Occupation' )
    
        return f
    
    def franckmatrix(self, f, axes, vminInput=0, vmaxInput=1):
        cax = axes.matshow(np.log10(self.franck), interpolation='nearest', vmin=vminInput, vmax=vmaxInput)   
        
        axes.set_title('$\log_{10}{|<0,n|s(x)|v,1>|^2}$', y = 1.08) 
        axes.set_xlabel('n')
        axes.set_ylabel('v')
        f.colorbar(cax)
        return cax
      
    def plot_current(self, axes , scale='lin', name=''):
 
        axes.set_xscale(scale)      
        axes.plot(self.parameter, self.current, linestyle='-', lw='2', label=name)
    
        #ax.set_xlabel('Voltage [V]')
        axes.set_ylabel('Current [$\mu$ A]')
        #axes.set_ylabel('Current nA')
        
        return axes

    def plot_current_t(self, axes , scale='lin', colorp="b", name='', siunits=True):
    
        axes.set_xscale(scale)
        
        if siunits:
            axes.plot(self.parameter, self.current, linestyle='-', color=colorp, lw='2', label=name)
            #ax.set_xlabel('Time [a.u.]')
            axes.set_ylabel('Current [$\mu$A]')
        else:
            axes.plot(self.parameter*self.au2second, self.current, color=colorp, linestyle='-', lw='2', label=name)
            #ax.set_xlabel('Seconds')
            axes.set_ylabel('Current [$\mu$A]')
        return axes
    
    def plot_position(self, axes , siunits=False, scale='lin', name=''):
        
        
        if siunits:
            axes.plot(self.parameter, self.position, linestyle='-', lw='2', label=name)
            axes.set_xscale(scale)
            axes.set_xlabel('Voltage [V]')
            #ax.set_ylabel('Current [$\mu$ A]')
            axes.set_ylabel('Position [a.u]')   
        else:
            axes.plot(self.parameter, self.position*self.bohrtoangstromtoangstrom, linestyle='-', lw='2', label=name)
            axes.set_xscale(scale)
            axes.set_xlabel('Voltage [V]')
            #ax.set_ylabel('Current [$\mu$ A]')
            axes.set_ylabel('Position [a.u]') 
            
           
        return axes
    
    def plot_position_t(self, axes , scale='lin', colorp = "b", siunits=True, name=''):
        
        axes.set_xscale(scale)       
        
        if siunits:
            axes.plot(self.parameter, self.position, linestyle='-', lw='2', color = colorp, label=name)
            axes.set_xlabel('Time [a.u]')
            axes.set_ylabel('Position [a.u]')  
        else:
            axes.plot(self.parameter*self.au2second, self.position*self.bohrtoangstrom, linestyle='-', color = colorp, lw='2', label=name)
            axes.set_xlabel('Time [s]')
            axes.set_ylabel('Position [$\AA$]')  
        return axes
    
    def plot_energy_t(self, axes , scale='lin', siunits=True, name=''):
        
        axes.set_xscale(scale)       
        
        if siunits:
            axes.plot(self.parameter, self.energy, linestyle='-', lw='2', label=name)
            axes.set_xlabel('Time [a.u]')
            axes.set_ylabel('Position [a.u]')  
        else:
            axes.plot(self.parameter*self.au2second, self.energy, linestyle='-', lw='2', label=name)
            axes.set_xlabel('Time in s')
            axes.set_ylabel('Position [a.u]')  
        return axes
      
    def plot_population(self, axes, pop_number=10, scale='lin'):
        
        axes.set_xscale(scale)
        axes.set_xlabel('Voltage [V]')
        axes.set_ylabel('Population')
        
        for i in range(1,pop_number):
        
            axes.plot(self.occupation[0]*self.au2second, self.occupation[i], linestyle='-', lw='2', label='State' + str(i-1))

        return axes
    
    def plot_notpopulation(self, axes, pop_number=10, scale='lin'):
        
        axes.set_xscale(scale)
        axes.set_xlabel('Voltage [V]')
        axes.set_ylabel('Not Population')
        
        for i in range(1,pop_number):
        
            axes.plot(self.unoccupation[0], self.unoccupation[i], linestyle='-', lw='2', label='State' + str(i-1))

        return axes
    
    def putexitationlines(self, axes, quanta=1, start=0, end=20):

        exitations, pair, lrange = self.exitation(start, end, quanta)
        
        [axes.axvline(_volt, linewidth=1) for _volt in exitations]

        axes.set_xticks(exitations)
        axes.set_xticklabels(pair , fontsize=7)
        
        
        return axes
    
    def putexitationslist(self, axes, exlist, inputcolor='b'):
        
        transition=[]
        pair =[]
        
        #Caclulate
        for element in exlist:       
            transition.append(2*(self.energy_occupied[element[1]]-self.energy_unoccupied[element[0]]))
            pair.append(str(element[0]) + '>' + str(element[1]))
            
        #  print element[0], element[1], element
            
        #Put into List
        [axes.axvline(_volt, linewidth=2, color=inputcolor) for _volt in transition]
        
        axes.set_xticks(transition)
        axes.set_xticklabels( pair , color = inputcolor, fontsize=7)
    
        return axes
    
    #Attention: Method works only for grid with a unit stepsize
    def derivate_energy(self):
    
        stepsize = np.average(np.diff(self.parameter))
        
        #New Grid which is shifted by the half stepsize
        #First temporary Calculation which has one extra grid ponts
        new_grid_temp = self.parameter +  stepsize / 2
        #Real grid which excludes the last item 
        new_grid = new_grid_temp[0:-1]
    
        # Calc Differences between values
        d_energy = np.diff(self.energy) / stepsize
        
        return (d_energy, new_grid)

#Attention: Method works only for grid with a unit stepsize
    def derivate_position(self):
    
        stepsize = np.average(np.diff(self.parameter))
        
        #New Grid which is shifted by the half stepsize
        #First temporary Calculation which has one extra grid ponts
        new_grid_temp = self.parameter +  stepsize / 2
        #Real grid which excludes the last item 
        new_grid = new_grid_temp[0:-1]
    
        # Calc Differences between values
        d_position = np.diff(self.position) / stepsize
        
        return (d_position, new_grid)
    
    def derivate_2_energy(self):
    
        d_energy, d_grid = self.derivate_energy()
        
        stepsize = np.average(np.diff(d_grid))
        _
        #New Grid which is shifted by the half stepsize
        #First temporary Calculation which has one extra grid ponts
        new_grid_temp = d_grid +  stepsize / 2
        #Real grid which excludes the last item 
        new_grid = new_grid_temp[0:-1]
    
        # Calc Differences between values
        dd_energy = np.diff(d_energy) / stepsize
        
        return (dd_energy, new_grid)
    
    def fft_position(self, axes, colorp = 'b'):
    
        time_step = np.average(np.diff(self.parameter))
        
        sample_freq = fftpack.fftfreq(len(self.position), d=time_step)
        
        position_fft = fftpack.fft(self.position)
        pidxs = np.where(sample_freq > 0 )
        freqs, power = sample_freq[pidxs], np.abs(position_fft)[pidxs]
        freq = freqs[power.argmax()]
        
        axes.plot(freqs, power, lw='3', color = colorp)
        axes.set_xlabel('Frequency [$\omega_0$]')
        axes.set_ylabel('Amplitude')
        
        return axes
    
    def fft_current(self, axes):
    
        time_step = np.average(np.diff(self.parameter))
        
        sample_freq = fftpack.fftfreq(len(self.current), d=time_step)
        
        current_fft = fftpack.fft(self.position)
        pidxs = np.where(sample_freq > 0 )
        freqs, power = sample_freq[pidxs], np.abs(current_fft)[pidxs]
        freq = freqs[power.argmax()]
        
        axes.plot(freqs, power, lw='3', color = 'r')
        axes.set_xlabel('Frequency [$\omega_0$]')
        axes.set_ylabel('Amplitude')
        
        return axes
    
    def fft_energy(self, axes):
    
        time_step = np.average(np.diff(self.parameter))
        
        sample_freq = fftpack.fftfreq(len(self.energy), d=time_step)
        
        energy_fft = fftpack.fft(self.energy)
        pidxs = np.where(sample_freq > 0 )
        freqs, power = sample_freq[pidxs], np.abs(energy_fft)[pidxs]
        freq = freqs[power.argmax()]
        
        axes.plot(freqs, power, lw='3', color = 'r')
        axes.set_xlabel('Frequency [$\omega_0$]')
        axes.set_ylabel('Amplitude')
        
        return axes
    
    
    def putexitationlines_fft(self, axes, fontsizep=7 ,quanta=1, start=0, end=20, colorp = 'b'):

        exitations, pair, lrange = self.exitation_fft(start, end, quanta)
         
        [axes.axvline(_volt, linewidth=1, color = colorp) for _volt in exitations]

        axes.set_xticks(exitations)
        axes.set_xticklabels(pair , fontsize=fontsizep)
        
        
        return axes
  
    def exitation_fft(self, lower_bound, upper_bound, quanta):
   
        transition = []
        pair=[]
   
        lrange = range(lower_bound, upper_bound)
        
        for i in lrange:
        
            transition.append((self.energy_occupied[i+quanta]-self.energy_occupied[i])*self.factor)
            pair.append(str(i) + '->' + str(i+quanta))


