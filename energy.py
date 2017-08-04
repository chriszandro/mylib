import numpy as np

au2second = 2.418884254e-17
au2femto = au2second*1e15
femto2au = 1/au2femto
au2ev = 27.21138
ev2au = 1/au2ev
eVtoHz = 2.41798945e14
Hztoau = 4.13413732914335e16
factor = eVtoHz / Hztoau
bohrtoangstrom = 0.529177249

class energy_inspector:

    def __init__(self, filename):
        self.energies = np.loadtxt(filename, usecols=(1,))
        return

    def get_trans(self, i, j):
        transition = self.energies[i] - self.energies[j]
        return transition

    def get_trans_au(self, i, j):
        transition = self.energies[i] - self.energies[j]
        return transition*factor

    def transition(self, N):

       return np.roll(self.energies, N) -  self.energies

    def putex(self, ax, state_shift=1, state_list=[], color="r", height=1):

        for i in state_list
            frequency = self.get_trans_au(state_shift+i, i)
            label_ed = "$\omega_{" + str(state_shift + i + 1) + "," +  str(i + 1)  + "}$"
            ax.axvline(frequency,color="r", lw=1.0)
            ax.text(frequency , height, label_ed, color="r", fontsize=18)

