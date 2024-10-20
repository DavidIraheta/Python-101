# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.
# from pathlib import Path

from pathlib import Path
#specify the folder to search
projects_folder = Path("/Users/davidiraheta/Documents/CodingNomads/Projects/python-101-main")
#search for python files in the projects folder
print("Python files found in the projects folder:\n")
for file in projects_folder.rglob("*.py"):
    print(f"Found: {file}")


                            

# labs_folder = Path("/Users/davidiraheta/Documents/CodingNomads/labs")
# for root, dirs, files in labs_folder.rglob("*.py"):
#     for file in files:
#         if file.suffix == ".py":
            # print(file)
#import the Path class from the pathlib module