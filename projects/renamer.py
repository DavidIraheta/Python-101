# Move and rename all .png files on your Desktop

# Identify all screenshots on your Desktop

# Create a new directory

# Move and rename all screenshots
import pathlib
desktop = pathlib.Path('/Users/davidiraheta/Desktop')
new_path = pathlib.Path('/Users/davidiraheta/Desktop/screenshots')
new_path.mkdir(exist_ok=True)
for filepath in desktop.iterdir():
    if filepath.suffix == '.png':
        new_filepath = new_path.joinpath(filepath.name)
        filepath.replace(new_filepath)
    print("All .png files have been moved and renamed in the 'screenshots' folder.")





