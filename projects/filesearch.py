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
from pathlib import Path
import os
folder = Path("/Users/davidiraheta/Desktop")
jpg_files = ()
file_extensions = ()
for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(".jpg"):
            jpg_files.append(os.path.join(root, file))
        file_extensions.append(os.path.splitext(file)[1])
print(jpg_files)
# print(set(file_extensions))
