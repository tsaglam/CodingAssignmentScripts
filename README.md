# Scripts for Code-based Assignments
Different scripts that help with managing/processing/grading code-based assignments.

## convertToUtf8.py
Script to batch convert all files in a directory (recursively) to UTF-8. The original encoding is guessed via `chardet`. If this encoding is not correct, many different encodings are brute-forced.
To deal with cases where the detected encoding is not correct but it works anyway, all non ASCII characters are removed from the converted files.

Currently, this script is hardcoded to only convert Java files.

Usage: `python convertToUtf8.py ./directory/path`

## removeAuthor.py
Script to recursively remove lines containing `@author` from all Java files within a specified directory. Currently hardcoded to use the folder `./submissions`.

## wrap_in_folders.py
Script to wrap all Java files in the current directory into one folder each named after the file (without the Java suffix). Basically converts single-file submissions to directory submissions for JPlag.
