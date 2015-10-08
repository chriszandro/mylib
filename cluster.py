# New Cluster program

#Class of the computation file
class computation:

    #Computation File Constructor retrieving parameters
    def __init__(self, computation_path="", computation_file="computation",
                 mode=1, plot_bool=1, rhox_bool=1, surf_bool=1, pop_bool=1, performance_bool = 0,
                 summary_bool = 1, coupling_bool=1, pop_number=10,
                 N=1500, dvr_method=1, fourier = 10.0e0, potential_id=0,
                 medim1=60, medim0=60, meBND=6, meBND_small=6,
                 system_output_filepath="./output/system",
                 summary_output_filepath="./output/summary",
                 result_output_filepath="./output/result",
                 evo_method=1, solve_method=2, abstol=1e-8, ideg=2, timebool=1,
                 xranges=8.0e0, appendbool = 0, performancebool=0, rhox_tolerance=1e-6,
                 fermion_bath=1,boson_bath=1,initialstate=1,
                 computation_modell=1, computation_modell_2=1):

        self.computation_path = computation_path
        self.computation_file = computation_file
        self.computation = self.computation_path + "/" + self.computation_file

        self.mode = mode
        self.plot_bool = plot_bool
        self.rhox_bool = rhox_bool
        self.surf_bool = surf_bool
        self.pop_bool = pop_bool
        self.pop_number = pop_number

        self.performance_bool = performance_bool
        self.summary_bool = summary_bool
        self.coupling_bool = coupling_bool

        self.N = N
        self.dvr_method = dvr_method
        self.fourier = fourier
        self.potential_id = potential_id
        self.medim1 = medim1
        self.medim0 = medim0
        self.meBND = meBND
        self.meBND_small = meBND_small
        self.system_output_filepath = system_output_filepath
        self.result_output_filepath = result_output_filepath
        self.summary_output_filepath = summary_output_filepath
        self.evo_method = evo_method
        self.solve_method = solve_method
        self.abstol = abstol
        self.ideg = ideg
        self.timebool = timebool
        self.xranges = xranges
        self.appendbool = appendbool
        self.performancebool = performancebool
        self.rhox_tolerance = rhox_tolerance
        self.fermion_bath = fermion_bath
        self.boson_bath = boson_bath
        self.initialstate =  initialstate

        self.computation_modell = computation_modell
        self.computation_modell_2 = computation_modell_2

    #Writing the computation file
    def write_computation_file(self):

        Computation = open(self.computation, "w")
        Computation.write("---------------Program Mode-------------------------------------\n")
        Computation.write("%20d" % self.mode + "           " +  "#Program-Mode | 1: Voltage-Loop\n")
        Computation.write("%20d" % self.plot_bool + "           " + "#Output System Generation: 0: No output, 1: Output\n")
        Computation.write("%20d" % self.rhox_bool + "           " + "#rhox Output 0: No output, 1: Output\n")
        Computation.write("%20d" % self.surf_bool + "           " + "#surface Output 0: No output, 1: Output\n")
        Computation.write("%20d" % self.pop_bool + "           " + "#population Output 0: No output, 1: Output\n")
        Computation.write("%20d" % self.summary_bool+ "           " + "# Performance File 0: No output, 1: Output\n")
        Computation.write("%20d" % self.performance_bool + "           " + "#Summary 0: No output, 1: Output\n")
        Computation.write("%20d" % self.coupling_bool  + "           " + "# Franck - Condon Matrix 0: No output, 1: Output\n")
        Computation.write("%20d" % self.pop_number+ "           " + "# Number of Population \n")
        Computation.write("---------------System-------------------------------------------\n")
        Computation.write("%20d" % self.N + "           " + "#Number of Grid Points N\n")
        Computation.write("%20d" % self.dvr_method + "           " + "#N \n")
        Computation.write("%20e" % self.fourier + "           " + "Fourier \n")
        Computation.write("%20d" % self.potential_id + "           " + "#id\n")
        Computation.write("--------------MasterEq-----------------------------------------\n")
        Computation.write("%20d" % self.medim0 + "           "  + "  #medim00          Dimension 00\n")
        Computation.write("%20d" % self.medim1 + "           " + "  #medim11          Dimension 11\n")
        Computation.write("%20d" % self.meBND + "           " + "  #meBand           Bandwidth\n")
        Computation.write("%20d" % self.meBND_small + "           " + "  #meBand           Bandwidth\n")
        Computation.write("----------------OuputPaths--------------------------------------\n")
        Computation.write("--- System output filepath\n")
        Computation.write(self.system_output_filepath + "\n")
        Computation.write("--- Summary output filepath\n")
        Computation.write(self.summary_output_filepath + "\n")
        Computation.write("--- Result output filepath\n")
        Computation.write(self.result_output_filepath + "\n")
        Computation.write("---------------Time Evolution-----------------------------------\n")
        Computation.write("%20d" % self.evo_method + "           " + "  #Evaluation Method (1=expokit chebjev, 2=zvode, 3=expokit pade)\n")
        Computation.write("%20d" % self.ideg + "           " + "  #Pade Coefficient for Calcs\n")
        Computation.write("---------------Schroedinger ------------------------------------\n")
        Computation.write("%20d" % self.ideg + "           " + "  #Logical for Eigensystem Routine for Schroedinger\n")
        Computation.write("%20d" % self.abstol + "           " + "\n")
        Computation.write("---------------------------ups -------------------------------\n")
        Computation.write("%20d" % self.timebool + "           " + "  #Boolean for timestamps in the outputfiles \n")
        Computation.write("%20e" % self.xranges + "           " + "xrange for the 3d plots \n")
        Computation.write("%20d" % self.appendbool + "           " + "append bool for performance testing\n")
        Computation.write("%20e" % self.rhox_tolerance + "           " + "tolerance parameter for the 3d plots\n")
        Computation.write("---------------------------Baths -------------------------------\n")
        Computation.write("%20d" % self.fermion_bath + "           " + "  #(=1 for including fermion both, 0 otherwise) \n")
        Computation.write("%20d" % self.boson_bath+ "           " + "(=1 for including harmonic bath, 0 otherwise \n")
        Computation.write("---------------------------Initial States -------------------------------\n")
        Computation.write("%20d" % self.initialstate + "           " + "Initial state for time evolution. 1 for conventinal switching. 2 for pure state\n")
        Computation.write("---------------------------Initial States -------------------------------\n")
        Computation.write("%20d" % self.computation_modell + "           " + "Computation Modell \n")
        Computation.write("%20d" % self.computation_modell_2 + "           " + "Computation Modell Paramter 2 \n")
        Computation.write("---------------End Of File------------------------------------\n")
        Computation.write("Modes: 1 CVC Mode bias-independent | 2 Varying Gate Voltage with constant voltage |\n 3 CVC with heatmaps | 4 CVC biasDEPENDENT |")
        Computation.write("20 Zvode Time Evolution | 30 Expokit Time Evolution |\n 50 Snaptshot Mode | 42...")
        Computation.close()

        print "Computation file written: " + self.computation

#Inputfile for physical parameters
class inputfile:

    #Constructor to obtain the parameters
    def __init__(self, inputfile_path="",
            inputfile_name="inputfile", l=1.25,
            delta=0.4, Vb=0.5, shiftEnergy=0.1,
            xshift=0.0, omega=1.0, lambdas=0.0,
            parabolashift=0.3,
            A=1.0, B=0.2, C=1.0, switchshift=0.0,
            grid_bias_voltage=10, start_bias_voltage=0.3, end_bias_voltage=0.3,
            grid_gate_voltage=100, start_gate_voltage=0.0, end_gate_voltage=1.8, d=1.0,
            Lj = 1, angle = 60, trans_shift = 1.0,
            beta1L=3.0, beta2L=0.1, beta1R=3.0, beta2R=0.1, T=293.0,
            fermi_level=0.0, time_grid=1000, time_start=0.0, time_end=1e3,
            rhox_step=1000, parameter_start=0, parameter_end=1000, parameter1=5,
            wcut=0.097, eta=0.0138,hbath_temp=293, 
            initial_occupation=0, initial_state_number=1, initial_state_number_2=2, 
            l_2=1.25, delta_2=0.1, Vb_2=0.5 ):

        self.Lj = Lj
        self.angle = angle
        self.trans_shift = trans_shift

        self.fermi_level = fermi_level

        self.time_grid = time_grid
        self.time_start = time_start
        self.time_end = time_end

        self.rhox_step = rhox_step

        self.parameter_start = parameter_start
        self.parameter_end = parameter_end

        self.beta1L = beta1L
        self.beta2L = beta2L

        self.beta1R = beta1R
        self.beta2R = beta2R

        self.T = T

        self.inputfile_name = inputfile_name
        self.inputfile_path = inputfile_path
        self.l = l
        self.delta = delta
        self.Vb = Vb
        self.shiftEnergy = shiftEnergy
        self.xshift = xshift
        self.omega = omega
        self.lambdas = lambdas
        self.parabolashift = parabolashift
        self.A = A
        self.B = B
        self.C = C
        self.switchshift = switchshift

        self.grid_bias_voltage = grid_bias_voltage
        self.start_bias_voltage = start_bias_voltage
        self.end_bias_voltage = end_bias_voltage

        self.grid_gate_voltage = grid_gate_voltage
        self.start_gate_voltage = start_gate_voltage
        self.end_gate_voltage = end_gate_voltage
        self.d = d

        self.wcut= wcut
        self.eta=eta
        self.hbath_temp=hbath_temp

        self.inputfile = self.inputfile_path + "/" + self.inputfile_name

        self.initial_occupation = initial_occupation
        self.initial_state_number= initial_state_number
        self.initial_state_number_2 =  initial_state_number_2
 
        self.l_2 = l_2
        self.delta_2 = delta_2
        self.Vb_2 = Vb_2

 #Writing the inputfile in given path
    def write_file(self):

        InputFile = open(self.inputfile, 'w')
        InputFile.write("-----------------------Potential----------------------------------------------" + "\n")
        InputFile.write("%20.10f" % self.l + "  #translocation length" + "\n")
        InputFile.write("%20.10f" % self.delta + "  #Delta + \n")
        InputFile.write("%20.10f" % self.Vb + "  #Barrier Height Vb" + "\n")
        InputFile.write("%20.10f" % self.shiftEnergy + "  # Energy shift between occupied and unoccupied Potential" + "\n")
        InputFile.write("%20.10f" % self.xshift + "   #x-shift" + "\n")
        InputFile.write("-----------------------Vibronic-----------------------------------------" + "\n")
        InputFile.write("%20.10f" % self.omega + "  #Omega (.1) " + "\n")
        InputFile.write("%20.10f" % self.lambdas + "  #Lambda (0.06)" + "\n")
        InputFile.write("%20.10f" % self.parabolashift + "  #Parabola Shift (.3)" + "\n")
        InputFile.write("-----------------------Switch Function-----------------------------------------" + "\n")
        InputFile.write("%20.10f" % self.A + "  #A" + "\n")
        InputFile.write("%20.10f" % self.B + "  #B" + "\n")
        InputFile.write("%20.10f" % self.C + "  #C" + "\n")
        InputFile.write("%20.10f" % self.switchshift + "  #switchShift" + "\n")
        InputFile.write("--------------- --------Voltage Grid---------------------) " + "\n")
        InputFile.write("%20d" % self.grid_bias_voltage + "  #Bias Grid" + "\n")
        InputFile.write("%20.10f" % self.start_bias_voltage + " #start voltage" + "\n")
        InputFile.write("%20.10f" % self.end_bias_voltage + " #end voltage" + "\n")
        InputFile.write("-----------------------Field Grid----------------------------------------------" + "\n")
        InputFile.write("%20d" % self.grid_gate_voltage + "  #Gate Grid" + "\n")
        InputFile.write("%20.10f" % self.start_gate_voltage + "  #Voltage gate1 (= intial Gate voltage!)" + "\n")
        InputFile.write("%20.10f" % self.end_gate_voltage + "  #Voltage gate2" + "\n")
        InputFile.write("%20.10f" % self.d + "  #d in nano meter" + "\n")
        InputFile.write("-----------------------Field in Dependance of V--------------------------------" + "\n")
        InputFile.write("%20.10f" % self.Lj + "  #Gate Grid" + "\n")
        InputFile.write("%20.10f" % self.angle + "  #Angle " + "\n")
        InputFile.write("%20.10f" % self.trans_shift + "  #transshift" + "\n")
        InputFile.write("-----------------------Self-Energy---------------------------------------------" + "\n")
        InputFile.write("------------Left- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -" + "\n")
        InputFile.write("%20.10f" % self.beta1L + "  #beta1" + "\n")
        InputFile.write("%20.10f" % self.beta2L + "  #beta2" + "\n")
        InputFile.write("                       #someday a new variable..." + "\n")
        InputFile.write("------------Right - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -" + "\n")
        InputFile.write("%20.10f" % self.beta1R + "  #beta1" + "\n")
        InputFile.write("%20.10f" % self.beta2R + "  #beta2" + "\n")
        InputFile.write("                       #someday a new variable..." + "\n")
        InputFile.write("------------Left & Right - - - - - - - - - - - - - - - - - - - - - - - - - - - -" + "\n")
        InputFile.write("%20.10f" % self.T + "  #Temperature" + "\n")
        InputFile.write("%20.10f" % self.fermi_level + "  #Fermi-Level" + "\n")
        InputFile.write("-----------------------Time Evolution- - - - - - - - - - - - - - - - - - - - - -" + "\n")
        InputFile.write(("%20d" % self.time_grid + "      #Time step") + "\n")
        InputFile.write(("%20.5e" % self.time_start).replace("e", "d") + "      #Time start in au" + "\n")
        InputFile.write(("%20.10e" % self.time_end).replace("e", "d") + "     #Time End in au" + "\n")
        InputFile.write("-----------------------Various Parameter Grid- - - - - - - - - - - - - - - - - -" + "\n")
        InputFile.write("%20d" % self.rhox_step + "  #Paramter Grid" + "\n")
        InputFile.write("%20.10f" % self.parameter_start + "  #Parameter 1" + "\n")
        InputFile.write("%20.10f" % self.parameter_end + "  #Parameter 2" + "\n")
        InputFile.write("-----------------------Harmonic Bath Parameters-----------------------------------" + "\n")
        InputFile.write("%20.10f" % self.wcut + "  #Wcut" + "\n")
        InputFile.write("%20.10f" % self.eta + "  #eta" + "\n")
        InputFile.write("%20.10f" % self.hbath_temp + "  #Temperature of the harmonic Bath" + "\n")
        InputFile.write("-----------------------Pure State Management-----------------------------------" + "\n")
        InputFile.write("%10d" % self.initial_occupation + "           " + "Initial occupation switching. 2 for pure state\n")
        InputFile.write("%10d" % self.initial_state_number + "           " + "Initial state number\n")
        InputFile.write("%10d" % self.initial_state_number_2 + "           " + "Second Initial state number\n")
        InputFile.write("-----------------------Second Set of Double Well Parameters--------------------" + "\n")
        InputFile.write("%20.10f" % self.l_2 + "  #2nd translocation length" + "\n")
        InputFile.write("%20.10f" % self.delta_2 + "  #2nd Delta + \n")
        InputFile.write("%20.10f" % self.Vb_2 + "  #2nd Barrier Height Vb" + "\n")
        InputFile.write("-----------------------END OF INPUTFILE-----------------------------------" + "\n")
        InputFile.write("")


class jobproject(computation):

    def __init__(self, name, program, programprojectpath, projectpath, *args, **kwargs):
        """
        Main Object to handle a jobproject. It prepares all necessary paths and folders. Subsequently it
        creates the computation file. The "joblist" array contains all jobs associated by the jobproject
        """

        from os.path import expanduser

        self.projectpath = projectpath
        self.programprojectpath = programprojectpath
        self.program = program
        self.name = name

        self.home = expanduser("~")

        self.mainpath =  self.projectpath + "/" + self.name

        # Paths
        self.resultpath =  self.mainpath + "/result"
        self.summarypath = self.mainpath + "/summary"
        self.systempath = self.mainpath + "/system"
        self.collectorpath = self.mainpath + "/collector"
        self.joboutpath = self.mainpath + "/joboutput"
        self.jobfilespath = self.mainpath + "/jobfiles"
        self.testscriptspath = self.programprojectpath + "/" + "testscripts" + "/" + self.name

        # Computation File
        self.computation_file = "computation" + "_" + self.name

        computation.__init__(self, system_output_filepath=self.systempath,
                             result_output_filepath=self.resultpath,
                             summary_output_filepath=self.summarypath,
                             computation_file=self.computation_file, computation_path=self.jobfilespath,
                             *args, **kwargs)

        self.joblist = []

        # Create Folder + Computation File
        self.create_project_folder()
        computation.write_computation_file(self)
        self.put_bash()

    def reset_jobs(self):
        """
        Empty the Joblist.
        """

        self.joblist[:] = []
        self.delete_project()

        self.create_project_folder()
        computation.write_computation_file(self)
        self.put_bash()

        pass

    def delete_project(self):
        """
        Deletes the folder associated to the project
        """

        import shutil
        import os
        # Delete Created Folders
        # --- Main Folder
        if os.path.exists(self.mainpath):
            shutil.rmtree(self.mainpath)

        # --- Testscriptspath
        if os.path.exists(self.testscriptspath):
            shutil.rmtree(self.testscriptspath)

    def add_job(self, number_bool=0, *args, **kwargs):
        """
        ADD a jobobject to the jobfilelist
        """

        jobnumber = len(self.joblist) + 1

        if number_bool==1: 
            jobname = self.name + str(jobnumber)
        else:
            jobname = self.name 

        job = job_rrze(name=jobname, programprojectname=self.programprojectpath, program=self.program, computation_file=self.computation_file,
                              jobfilespath=self.jobfilespath, joboutpath=self.joboutpath, *args, **kwargs)

        self.joblist.append(job)

    def print_job_list(self):
        """
        Print out the added jobs for check
        """

        for job in self.joblist:
            print job.name

    def put_jobproject(self):
        """
        Finishes te Jobproject
        """

        for job in self.joblist:
            job.put_job()

        self.put_testscripts()

        pass

    def put_job_file_merger(self):

        path = self.resultpath + "/filename.list" 

        namefile = open(path, 'w')

        for job in self.joblist:
            namefile.write(job.name)

        namefile.close()

        pass

    def put_testscripts(self):
        """
        This script writes a small bash script into the testscript folder to perform a test
        """

        for job in self.joblist:
            #---------------------------------------
            # Testscript Folder
            #---------------------------------------
            # Create a Test file to execute the created inputfile easily

            path = self.testscriptspath + "/" + job.name + ".sh"
            Testscript = open(path, 'w')
            Testscript.write("#!/bin/bash\n")
            Testscript.write("#Program to execute current inputfile \n")
            Testscript.write(job.execution)
            Testscript.close()

            #print "Testscript in: " +  path

    def put_local_jobscript(self, path="./jobstarters"):
            """
            Creates bash scripts in to the "path" folder which executes all jobs created by the jobproject
            """

            import os

            if not os.path.exists(path):
                os.makedirs(path)

            # Create Bash File for job execution
            Jobsubmit = open(path + "/" + self.name + "_jobstart.sh", 'w')
            Jobsubmit.write("#!/bin/bash \n")
            Jobsubmit.write("echo \"Processing" + self.name + "\" \n ")

            for job in self.joblist:
                submitt_string = "qsub " + job.jobfile
                Jobsubmit.write(submitt_string + "\n")
                Jobsubmit.write("sleep 2 \n")

            Jobsubmit.close()

    def put_runscript(self):

            runscript = open(self.jobfilespath + "/runscript.sh", 'w')

            for job in self.joblist:
                execute = "./" +job.program + " " + job.inputfile_name + " " + job.computation_file 
                runscript.write(execute + "\n")
                runscript.write("sleep 2 \n")

            runscript.close()

            runscript_neg = open(self.jobfilespath + "/runscript_neg.sh", 'w')

            for job in self.joblist:
                execute = "#./" +job.program + " " + job.inputfile_name + " " + job.computation_file 
                runscript_neg.write(execute + "\n")
                runscript_neg.write("#sleep 2 \n")
            runscript_neg.close()

    def create_project_folder(self):
        """
        Creates all necessary folders
        """

        import os
        # Create Folders
        # --- result
        if not os.path.exists(self.summarypath):
            os.makedirs(self.summarypath)
        # --- system
        if not os.path.exists(self.systempath):
            os.makedirs(self.systempath)
        # --- result
        if not os.path.exists(self.resultpath):
            os.makedirs(self.resultpath)
        # --- joboutputpath
        if not os.path.exists(self.joboutpath):
            os.makedirs(self.joboutpath)
        # --- Jobfiles
        if not os.path.exists(self.jobfilespath):
            os.makedirs(self.jobfilespath)
        # --- Testscriptspath
        if not os.path.exists(self.testscriptspath):
            os.makedirs(self.testscriptspath)

    def put_bash(self):
      Jobsubmit = open(self.jobfilespath + "/" + "jobsubmit.sh", 'w')
      Jobsubmit.write("#!/bin/bash \n")
      Jobsubmit.write("for FILE in *.job; do \n")
      Jobsubmit.write("echo \"Processing $FILE \" \n ")
      Jobsubmit.write("qsub ${FILE}\n")
      Jobsubmit.write("sleep 3\n")
      Jobsubmit.write("done")
      Jobsubmit.close()
        #---------------------------------------
            # SMALL Bash Script to submitt all Jobs
        #---------------------------------------

        # Create Bash File for job execution

#Class for the jobfile a the RRZE Computing systems
class job_rrze(inputfile):

    def __init__(self, name, programprojectname, program, computation_file, jobfilespath, joboutpath, specific="", subfolder="", cluster="lima", time="24:00:00", *args, **kwargs):

        # Read In
        self.name = name + specific
        self.program = program
        self.programprojectname = programprojectname
        self.computation_file = computation_file
        self.jobfilespath = jobfilespath
        self.joboutpath = joboutpath
        self.cluster = cluster
        self.time = time
        self.subfolder=subfolder

        self.inputfile = "inputfile_" + self.name + ".inp"
        self.jobfile = self.jobfilespath + "/" + self.name + ".job"

        if self.cluster == "lima":
            self.cores = "24"
        elif self.cluster == "emmy":
            self.cores = "40"

        # RESOURCES
        #---Threads MKL
        self.mkldynamic = "export MKL_DYNAMIC=true"
        self.mklnumthreads = "export MKL_NUM_THREADS=" + self.cores

        #---OpenMP
        self.kmpaffinity = "#export KMP_AFFINITY=disabled"
        self.ompdynamic = "#export OMP_DYNAMIC=false"
        self.ompnumthreads = "#export OMP_NUM_THREADS=6"

        self.resource1 = "#PBS -l nodes=1:ppn=" + self.cores
        self.resource2 = "#PBS -l walltime=" + self.time

        # JobFile
        self.jobName = "#PBS -N " + self.name
        self.jobOutput = "#PBS -o " + self.joboutpath + "/" + "${PBS_JOBNAME}.log"
        self.jobError = "#PBS -e " + self.joboutpath + "/" + "${PBS_JOBNAME}.err"

        self.moduleLoad = "module load intel64"
        self.changeDirectory = "cd " + self.programprojectname

        self.execution = self.program + " " + self.inputfile + " " + self.computation_file + " " + self.jobfilespath + "/"

        inputfile.__init__(self, inputfile_path=self.jobfilespath, inputfile_name=self.inputfile, *args, **kwargs)

        pass

    def put_job(self):

        # Write the inputfile
        inputfile.write_file(self)
        # Write the jobfile
        self.write_job_file()

    def run_job(self):

        import os

        command = "qsub " + self.jobfile

        print "Execution of: " + self.jobfile
        os.system(command)


    def write_job_file(self):

        JobFile = open(self.jobfile, "w")
        JobFile.write("#!/bin/bash -l" + "\n")
        JobFile.write('#' + "\n")
        JobFile.write('# Resources' + "\n")
        JobFile.write(self.resource1 + "\n")
        JobFile.write(self.resource2 + "\n")
        JobFile.write("\n")

        JobFile.write('# Job Specifications' + "\n")
        JobFile.write('# Job Name' + "\n")
        JobFile.write(self.jobName + "\n")
        JobFile.write("\n")
        JobFile.write('# Job Output' + "\n")
        JobFile.write(self.jobOutput + "\n")
        JobFile.write(self.jobError + "\n")
        JobFile.write("\n")
        JobFile.write("#Mail with (a)bort, (b)egin, (e)nd" + "\n")
        JobFile.write("#PBS -m ae" + "\n")
        JobFile.write("\n")
        JobFile.write('# Job Execution' + "\n")
        JobFile.write("#OpenMP" + "\n")
        JobFile.write(self.kmpaffinity + "\n")
        JobFile.write(self.ompdynamic + "\n")
        JobFile.write(self.ompnumthreads + "\n")
        JobFile.write("\n")
        JobFile.write("#Threads MKL" + "\n")
        JobFile.write(self.mkldynamic + "\n")
        JobFile.write(self.mklnumthreads + "\n")
        JobFile.write('# Module Load' + "\n")
        JobFile.write(self.moduleLoad + "\n")
        JobFile.write("\n")
        JobFile.write('# Change Directory' + "\n")
        JobFile.write(self.changeDirectory + "\n")
        JobFile.write("\n")
        JobFile.write('# Run' + "\n")
        JobFile.write(self.execution)
        JobFile.close()

        pass
