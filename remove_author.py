import os
import sys


def remove_author_lines(file_path):
    """
    Remove lines containing '@author' from the specified file.
    """
    print(file_path)
    lines_to_keep = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if "@author" not in line:
                lines_to_keep.append(line)
            else:
                print(" - remove " + line)

    with open(file_path, "w", encoding="utf-8") as file:
        for line in lines_to_keep:
            file.write(line)


def process_directory(directory):
    """
    Recursively process all files in the specified directory and its subdirectories,
    removing lines containing '@author' from Java files.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                if file_path.endswith(".java"):
                    remove_author_lines(file_path)


def main():
    if len(sys.argv) != 2:
        print("Usage: python remove_author.py directory_path")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)

    process_directory(directory)
    print("Author lines have been removed from the files in the directory.")


if __name__ == "__main__":
    main()
