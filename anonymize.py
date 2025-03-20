import pathlib
import argparse

student_id_map = {}  # unique identifiers to number


def anonymize_datasets(base_path: pathlib.Path, separator: str):
    for dataset in base_path.iterdir():
        if dataset.is_dir():
            anonymize(dataset, separator)


def anonymize(dataset_path: pathlib.Path, separator: str):
    for folder in dataset_path.iterdir():
        if folder.is_dir():
            identifier = get_identifier(folder.name, separator)
            if identifier not in student_id_map:
                student_id_map[identifier] = len(student_id_map) + 1

            new_name = f"student{student_id_map[identifier]}"
            new_path = dataset_path / new_name

            if not new_path.exists():
                folder.rename(new_path)


def get_identifier(folder_name: str, separator: str):
    parts = folder_name.rsplit(separator, 1)
    if len(parts) > 1:
        return parts[-1]  # return identifier
    raise ValueError(f"'{separator}' not found in '{folder_name}'")


def main():
    parser = argparse.ArgumentParser(
        description="Rename files and folders by replacing the last occurrence of a separator."
    )
    parser.add_argument(
        "path", type=str, help="Path to the directory containing the folders."
    )
    parser.add_argument(
        "separator",
        type=str,
        help="Separator character to split names. String after last occurence is used as identifier.",
    )
    args = parser.parse_args()
    path = pathlib.Path(args.path)

    anonymize_datasets(path, args.separator)


if __name__ == "__main__":
    main()
