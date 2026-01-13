import os

allfiles = []

# https://www.geeksforgeeks.org/python/python-list-all-files-in-directory-and-subdirectories/
def list_files_recursive(path='.'):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            list_files_recursive(full_path)
        else:
            allfiles.append(full_path)

list_files_recursive()

for i in allfiles:
    if ".html" in i:
        print(i)