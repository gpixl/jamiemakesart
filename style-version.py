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

print("Confirm all changes to all HTML files!!")

filetype = input("File (with extension):\n")

if len(filetype) < 2:
    quit()

oldVersion = input("Old version:\n")
newVersion = input("New version:\n")

changedFiles = 0
for i in allfiles:
    if ".html" in i:
        thisfile = open(i).read()

        if filetype + "?v=" + str(oldVersion) + "\"" in thisfile:
            changedFiles += 1
            thisfile = thisfile.replace(filetype + "?v=" + str(oldVersion) + "\"",filetype + "?v=" + str(newVersion) + "\"")
            with open(i, "w") as f:
                f.write(thisfile)

print("Changed " + str(changedFiles) + " files")