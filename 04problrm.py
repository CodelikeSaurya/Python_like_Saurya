import os

# specify the directory path
directory_path = "."  # "." means current directory

# get the list of files and directories
contents = os.listdir(directory_path)

# print the contents
print("Contents of the directory:", directory_path)
for item in contents:
    print(item)
