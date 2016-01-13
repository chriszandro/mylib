import subprocess


index_start = 513491 
index_end = 513606 

for i in range(index_start, index_end):
    command_string = "qdel"
    subprocess.call([command_string, str(i)], shell=False)
