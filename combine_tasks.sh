#!/bin/bash

readonly OUTPUT_FOLDER="CombinedTasks"
mkdir -p "$OUTPUT_FOLDER"

# Loop through each folder
for task_folder in */; do
    task_name=$(basename "$task_folder")

    # Skip the output folder
    if [ "$task_name" = "$OUTPUT_FOLDER" ]; then
        continue
    fi

    for submission_folder in "$task_folder"*/; do
        submission_name=$(basename "$submission_folder")
        identifier=${submission_name:(-5)}
        mkdir -p "$OUTPUT_FOLDER/$identifier"

        # Copy the submission folder to the corresponding identifier folder
        cp -R "$submission_folder" "$OUTPUT_FOLDER/$identifier/$task_name"
    done
done
