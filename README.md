# Scripts for Teaching Programming/Programming Assignments
Different scripts that help with managing/processing/grading code-based assignments.

## convert_to_utf8.py
Script to batch-convert all files in a specified directory (recursively) to UTF-8. The original encoding is guessed via `chardet`. If this encoding is not correct, many different encodings are brute-forced.
To deal with cases where the detected encoding is incorrect but works anyway, all non-ASCII characters are removed from the converted files.

Usage: `python convert_to_utf8.py ./path/to/dir/ file_extension`

## remove_author.py
Script to recursively remove lines containing `@author` from all Java files within a specified directory.

Usage: `python remove_author.py ./path/to/dir/`

## text_assignment_statistics.py

Script to count the frequency of answers in a text-based assignment. Takes a directory containing multiple text files, computing the most frequent answers. Ignores line breaks and trailing/leading spaces. Write the result in a CSV file located in the working directory.

Usage: `python text_assignment_statistics.py ./path/to/dir/`

## wrap_in_folders.py
Script to wrap all files of a particular type in a specified directory into one folder, each named after the file (without the file extension). Basically converts single-file submissions to directory submissions for [JPlag](https://github.com/jplag/JPlag).

Usage: `python wrap_in_folders.py ./path/to/dir/ file_extension`

### Input
```shell
directory
├─ a.java
└─ b.java
```

### Output
```shell
directory
├─ a
│  └─ a.java
└─ b
   └─ b.java
```

## combine_tasks.sh

Script to merge code for several assignments/subtasks. It combines all the tasks in the current working directory into identifier-specific (last five characters) folders in the result folder named CombinedTasks.

### Input
```shell
directory
├─ A
│  ├─ xyz-alice
│  └─ abc-bobby
└─ B
   ├─ uvw-alice
   ├─ jkl-bobby
   └─ dfg-chris
```

### Output
```shell
CombinedTasks
├─ alice
│  ├─ A
│  └─ B
├─ bobby
│  ├─ A
│  └─ B
└─ chris
   └─ B
```
