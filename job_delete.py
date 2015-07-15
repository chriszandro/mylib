import subprocess

index_start = 395323
index_end = 395361

for i in range(index_start, index_end):
    command_string = "qdel"
    subprocess.call([command_string, str(i)], shell=False)
