import os
import sys
import codecs
import chardet


def detect_encoding(file_path):
    with open(file_path, "rb") as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        return result["encoding"]


def get_all_encodings():
    try:
        all_encodings = codecs.lookup("")
        return [encoding for encoding in all_encodings]
    except LookupError as e:
        print(f"Error getting encodings: {e}")
        return []


def convert_content_to_utf8(content):
    # Convert content to UTF-8
    content_utf8 = content.encode("utf-8", "ignore").decode("utf-8")
    # Remove non-ASCII characters
    content_cleaned = "".join(char for char in content_utf8 if ord(char) < 128)
    return content_cleaned


def write_to_file(file_path, content):
    # Write the converted content back to the file with UTF-8 encoding and removed non-ASCII characters
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def convert_file(file_path, detected_encoding):
    try:
        with open(file_path, "r", encoding=detected_encoding) as file:
            content = file.read()
        content_cleaned = convert_content_to_utf8(content)
        write_to_file(file_path, content_cleaned)
        print(f"Converted: {file_path}")
        return True
    except (UnicodeDecodeError, LookupError):
        return False


def convert_to_utf8(file_path, found_encodings):
    detected_encoding = detect_encoding(file_path)
    if detected_encoding:
        found_encodings[detected_encoding] = (
            found_encodings.get(detected_encoding, 0) + 1
        )

    if convert_file(file_path, detected_encoding):
        return

    all_encodings = [detected_encoding] + get_all_encodings()

    for encoding in all_encodings:
        if encoding != detected_encoding and convert_file(file_path, encoding):
            return

    print(f"Error converting {file_path}")


def convert_java_files(directory):
    found_encodings = {}
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".java"):
                file_path = os.path.join(root, file_name)
                convert_to_utf8(file_path, found_encodings)

    print("\nFound Encodings (Sorted by Frequency):")
    sorted_encodings = sorted(found_encodings.items(), key=lambda x: x[1], reverse=True)
    for encoding, count in sorted_encodings:
        print(f"{encoding}: {count}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python convertToUtf8.py directory_path")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)

    convert_java_files(directory)


if __name__ == "__main__":
    main()
