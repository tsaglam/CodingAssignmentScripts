# Scripts for Code-based Assignments
Different scripts that help with managing/processing/grading code-based assignments.

## convertToUtf8.py
Script to batch convert all files in a directory (recursively) to UTF-8. The original encoding is guessed via `chardet`. If this encoding is not correct, many different encodings are brute-forced.
To deal with cases where the detected encoding is not correct but it works anyway, all non ASCII characters are removed from the converted files.

Currently, this script is hardcoded to only convert Java files.

Usage: `python convertToUtf8.py ./directory/path`

## removeAuthor.py

TODO
