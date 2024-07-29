import os
import shutil

# Get the current working directory
current_dir = os.getcwd()

# Iterate over all files in the current directory
for file_name in os.listdir(current_dir):
    if file_name.endswith('.java'):
        folder_name = file_name[:-5]
        
        # Create a new folder with the name of the file (without .java)
        new_folder_path = os.path.join(current_dir, folder_name)
        os.makedirs(new_folder_path, exist_ok=True)
        
        # Move the .java file into the new folder
        old_file_path = os.path.join(current_dir, file_name)
        new_file_path = os.path.join(new_folder_path, file_name)
        shutil.move(old_file_path, new_file_path)

print("Java files have been moved to their respective subfolders.")
