import os
import subprocess


def merge_files_in_folder(folder):
    for subdir, dirs, files in os.walk(folder):
        normed_path = os.path.normpath(subdir)
        if (os.path.basename(normed_path)) == "result":
            spec = normed_path.split(os.sep)[-2]
            print("Processing: ", spec)
            os.chdir(subdir)
            command = 'cat $(ls -v) > merged_' + spec
            subprocess.Popen([command])
