#!/bin/bash

# Specify the subdirectory name
DIRECTORY="games/"

# Create the directory if it doesn't exist
mkdir -p "${DIRECTORY}"

# Read the list of files from the input file
while IFS= read -r file; do
  # Create the file in the specified subdirectory
  touch "${DIRECTORY}${file}"
done < "test_input.txt"
