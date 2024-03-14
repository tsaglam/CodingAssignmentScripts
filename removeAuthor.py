import os

def remove_author_lines(file_path):
    print(file_path)
    lines_to_keep = []
    with open(file_path, 'r') as file:
        for line in file:
            if "@author" not in line:
                lines_to_keep.append(line)
            else:
                print(" - remove "+line)
    
    with open(file_path, 'w') as file:
        for line in lines_to_keep:
            file.write(line)

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                if file_path.endswith('.java'):
                    remove_author_lines(file_path)

if __name__ == "__main__":
    target_directory = "./submissions"  # Replace this with the path to your target directory
    process_directory(target_directory)
    print("Author lines have been removed from the files in the directory.")
