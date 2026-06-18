#!/bin/bash
# This script converts all Jupyter notebooks in the current directory and its subdirectories to Markdown format, while excluding specified directories.
# It ignores the 'sources' directory and the '.git' directory to prevent unnecessary conversions and potential issues with version control.

find . -name "*.ipynb" -type f -not -path "./sources/*" -not -path "./.git/*" -exec sh -c '
    for notebook do
        echo "Converting $notebook to Markdown..."
        jupyter nbconvert --to markdown "$notebook"
    done
' sh {} +
