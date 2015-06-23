import subprocess

index_start = 1713668
index_end = 1713780

for i in range(index_start, index_end):
    command_string = "qdel"
    subprocess.call([command_string,str(i)], shell=False)
