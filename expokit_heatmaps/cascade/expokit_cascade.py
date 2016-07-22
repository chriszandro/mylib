import cluster
import math
import time
import os
import list_creator as list_creator
import analysis
from shutil import copyfile
from subprocess import call
import numpy as np
import human_readable as human

temp = [10,293]
env = [0, 0.001]
bias = [0.0, 0.3, 0.7]

for T in temp:
    for en in env:
        for b in bias:
            string = ""
            string += "_B_" + str(b)
            string += human.human_readable_temperature(T)
            string += human.human_readable_environment(en)

            print (string)

