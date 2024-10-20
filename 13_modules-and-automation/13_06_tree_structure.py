# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.
from pathlib import Path
labs_folder = Path("/Users/davidiraheta/Documents/CodingNomads/labs")
for root, dirs, files in labs_folder.rglob("*.py"):
    for file in files:
        if file.suffix == ".py":
            print(file)

#

                            

