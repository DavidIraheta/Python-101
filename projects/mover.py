# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib

# Find the path to my Desktop

# Create a new folder

# Filter for screenshots only

# Create a new path for each file

# Move the screenshot there
from pathlib import Path
import os
desktop = Path.home().joinpath("Desktop")   
# print(desktop)
desktop.joinpath("Screenshots").mkdir(exist_ok=True)
for f in desktop.iterdir():
    if f.is_file() and f.suffix == ".png":
        f.replace (desktop.joinpath("Screenshots").joinpath(f.name))
