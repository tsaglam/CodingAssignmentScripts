import os
import sys
import shutil


def wrap_files(current_dir, extension):
    count = 0
    for file_name in os.listdir(current_dir):
        if file_name.endswith(extension):
            folder_name = file_name.remove(extension)

            # Create a new folder with the name of the file (without .java)
            new_folder_path = os.path.join(current_dir, folder_name)
            os.makedirs(new_folder_path, exist_ok=True)

            # Move the file into the new folder
            old_file_path = os.path.join(current_dir, file_name)
            new_file_path = os.path.join(new_folder_path, file_name)
            shutil.move(old_file_path, new_file_path)

            count += 1

    print(f"{count} {extension} files have been moved to their respective subfolders.")


def main():
    if len(sys.argv) != 3:
        print("Usage: python wrap_in_folders.py directory_path")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)

    file_extension = sys.argv[2]

    wrap_files(directory, file_extension)


if __name__ == "__main__":
    main()
