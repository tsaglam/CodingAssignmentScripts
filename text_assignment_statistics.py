import os
import csv
import sys
from collections import Counter


def strip_answer(answer):
    return answer.replace("\r", "").replace("\n", "").strip()


def count_answers(folder_path, output_file="results.csv"):
    txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
    answer_counter = Counter()

    for txt_file in txt_files:
        file_path = os.path.join(folder_path, txt_file)
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        processed_answer = strip_answer(content)
        answer_counter.update([processed_answer])

    sorted_answers = answer_counter.most_common()

    with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Answer", "Frequency"])

        for answer, frequency in sorted_answers:
            csv_writer.writerow([answer, frequency])

    print(f"Results written to {output_file}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python text_assignment_statistics.py directory")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)

    output_file = "results.csv"
    count_answers(directory, output_file)


if __name__ == "__main__":
    main()
