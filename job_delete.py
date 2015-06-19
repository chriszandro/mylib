import subprocess

index_start = 1711581
index_end = 1712243

for i in range(index_start, index_end):
    command_string = "qdel"
    subprocess.call([command_string,str(i)], shell=False)
