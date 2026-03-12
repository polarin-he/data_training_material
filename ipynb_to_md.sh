#!/bin/bash
# This script converts all Jupyter notebooks in the current directory and its subdirectories to Markdown format, while excluding specified directories. It also excludes any directory stated in the .gitignore file.

#!/bin/bash

# Read .gitignore and extract directory patterns
EXCLUDE_DIRS=()
while IFS= read -r line; do
    # Skip comments and empty lines
    if [[ "$line" =~ ^#.*$ || -z "$line" ]]; then
        continue
    fi
    # If the line ends with '/', it's a directory
    if [[ "$line" =~ .*/$ ]]; then
        EXCLUDE_DIRS+=("./$line*")
    fi
done < .gitignore

# Add default exclusions (e.g., .git)
EXCLUDE_DIRS+=("./.git/*")

# Build the 'find' command
FIND_CMD="find . -name \"*.ipynb\" -type f"
for dir in "${EXCLUDE_DIRS[@]}"; do
    FIND_CMD+=" -not -path \"$dir\""
done

# Execute the find command and convert notebooks
eval "$FIND_CMD" -exec sh -c '
    for notebook do
        echo "Converting $notebook to Markdown..."
        jupyter nbconvert --to markdown "$notebook"
    done
' sh {} +
