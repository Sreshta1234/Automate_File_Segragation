import os
import shutil

path = "Downloads"
print("Before copying files")

print(os.listdir(path))

source = "/Downloads/feather.png"
dest = '/Downloads/copyfeather.png'

destination = shutil.copy(source, dest)


