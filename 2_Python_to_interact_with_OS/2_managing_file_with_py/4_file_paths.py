# create a new directory

import os

new_dir = "package"
# os.mkdir(new_dir)
print(f"Directory '{new_dir}' created successfully.")  
# # To remove a directory, use the rmdir() method.
# # This method will only remove empty directories.
# # If the directory is not empty, you need to remove all files and subdirectories first.
# os.rmdir(new_dir) 


# Listing files and Directories
# IT will list all files and directories in the current directory (We can put any file path here)
items = os.listdir('.')
print(items)




# Joining Paths
dir_name = "folder"
file_name = "file.txt"
# os.getcwd() returns the current working directory full path
# os.path.join() joins the directory name and file name into a full path
# This is useful for creating file paths that are compatible with different operating systems.
full_path = os.path.join(os.getcwd(),dir_name, file_name)
print(full_path)  # Output: folder/file.txt

