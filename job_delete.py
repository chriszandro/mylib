import subprocess


index_start = 1765000 
index_end = 1768692 

for i in range(index_start, index_end):
    command_string = "qdel"
    subprocess.call([command_string, str(i)], shell=False)
