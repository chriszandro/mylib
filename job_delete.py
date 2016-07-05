import subprocess

index_start = 624639
index_end = 624873

for i in range(index_start, index_end):
    command_string = "qdel"
    subprocess.call([command_string, str(i)], shell=False)



