import subprocess

index_start = 1716244
index_end = 1716316

for i in range(index_start, index_end):
    command_string = "qdel"
    subprocess.call([command_string,str(i)], shell=False)
