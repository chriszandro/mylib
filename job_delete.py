import subprocess

index_start = 645724 
index_end = 645756 

for i in range(index_start, index_end):
    command_string = "qdel"
    subprocess.call([command_string, str(i)], shell=False)
