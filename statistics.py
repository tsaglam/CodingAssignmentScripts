import os
import csv
from collections import Counter

def preprocess_answer(answer):
    # Remove new lines and leading/trailing whitespace
    return answer.replace('\n', '').strip()

def count_answers(folder_path, output_file='results.csv'):
    # Get a list of all text files in the specified folder
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

    # Initialize a Counter to store the frequency of each answer
    answer_counter = Counter()

    # Iterate through each text file
    for txt_file in txt_files:
        file_path = os.path.join(folder_path, txt_file)

        # Read the content of the file as a single string
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Preprocess the answer before updating the counter
        processed_answer = preprocess_answer(content)

        # Update the counter with the frequency of each answer
        answer_counter.update([processed_answer])

    # Sort the answers by frequency in descending order
    sorted_answers = answer_counter.most_common()

    # Write results to a CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Answer', 'Frequency'])

        for answer, frequency in sorted_answers:
            csv_writer.writerow([answer, frequency])

    print(f'Results written to {output_file}')

if __name__ == "__main__":
    # Replace 'path/to/your/folder' with the actual path to your folder containing text files
    folder_path = '.'

    # Specify the output file name
    output_file = 'results.csv'

    count_answers(folder_path, output_file)
