# Write a script that searches a folder you specify (as well as its subfolders, up
# to two levels deep) and compiles a list of all `.jpg` files contained in there.
# The list should include the complete path of each `.jpg` file.
# 
# You should train:
# 
# - Using `for` loops
# - Using conditional statements
# - Working with `pathlib`
# - Thinking about nested loops
# 
# If you are feeling bold, create a list containing each type of file extension
# you find in the folder.
# Start with a small folder to make it easy to check whether your program is
# working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.
# from pathlib import Path

# Specify the folder to search
from pathlib import Path
folder = Path("/Users/davidiraheta/Documents/CodingNomads/Projects/python-101-main")
# set lists to hold jpg files and extensions
jpg_files = []
file_extensions = set()  # Use a set to avoid duplicates
# Traverse the folder up to two levels deep
for subfolder in folder.glob('*/*'):
    for file in folder.iterdir():
        if file.is_file():
            # Check for .jpg files and append their full path
            if file.suffix == ".jpg":
                jpg_files.append(str(file))
            # Add the file extension to the set
            file_extensions.add(file.suffix)
# Print the list of found .jpg files
print("List of .jpg files found:\n", jpg_files)# Print unique file extensions
print("\nUnique file extensions found:\n", file_extensions)




# from pathlib import Path
# import os
# folder = Path("/Users/davidiraheta/Documents/CodingNomads/Projects/python-101-main")
# jpg_files = ()
# file_extensions = set()
# for subfolder in folder.glob("*/*"):
#     for subfolder in subfolder.iterdir():
#         if __file__.is_file():
#             if __file__.suffix == ".jpg":
#                 jpg_files.append(str(file))
#                 file_extensions.add(file.suffix)
# print("List of .jpg files found in the folder:\n",jpg_files)
# print("n/Unique file extensions found in the folder:\n", file_extensions)



# for root, dirs, files in os.walk(folder):
#     for file in files:
#         if file.endswith(".jpg"):
#             jpg_files.append(os.path.join(root, file))
#         file_extensions.append(os.path.splitext(file)[1])
# print(jpg_files)
# # print(set(file_extensions))
