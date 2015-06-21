import subprocess

index_start = 1712643
index_end = 1712694

for i in range(index_start, index_end):
    command_string = "qdel"
    subprocess.call([command_string,str(i)], shell=False)
