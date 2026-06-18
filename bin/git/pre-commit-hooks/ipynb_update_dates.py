"""
Script: ipynb_update_dates.py
Description:
    This script automatically updates the "Date last modified" line in a Jupyter Notebook's Markdown cell
    with the current date (in DD-MM-YYYY format) whenever changes are pushed to Git.
    It is designed to be run as a Git pre-commit hook to ensure the date is always up-to-date.

Usage:
    1. Place this script in your repository.
    2. Set up a Git pre-commit hook to run this script before committing changes.
    3. Ensure the notebook file path and the target Markdown cell line are correctly specified.

Dependencies:
    - Python 3.x
    - JSON module (built-in)

Example Git Hook Setup:
    - Create a pre-commit hook in `.git/hooks/pre-commit`:
    #!/bin/bash

    # This pre-commit hook performs the following actions:
    # 1. Updates the dates in the Markdown files to reflect the current date.
    # 2. Adds all the generated Jupyter notebook to the staging area for commit.

    # Print the current working directory for debugging purposes
    echo "Pre-commit hook running in $(pwd)" >&2

    # Execute the script to convert Jupyter notebooks to Markdown
    bash /bin/git/pre-commit-hooks/ipynb_to_md.sh

    # Execute the script to update dates in the Markdown files
    python /bin/git/pre-commit-hooks/ipynb_update_dates.py

    # Add all the generated Markdown files to the staging area for commit
    find . -name "*.md" -exec git add {} \;

    # Add all the generated Jupyter notebook to the staging area for commit
    find . -name "*.ipynb" -exec git add {} \;
"""

import json
from datetime import datetime

# Path to your Jupyter Notebook file
notebook_path = "your_notebook.ipynb"

# Load the notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    notebook = json.load(f)

# Current date in the format you want (e.g., DD-MM-YYYY)
current_date = datetime.now().strftime("%d-%m-%Y")

# Iterate through the cells to find and update the Markdown cell
for cell in notebook["cells"]:
    if cell["cell_type"] == "markdown":
        for i, line in enumerate(cell["source"]):
            if "**Date last modified:" in line:
                # Update the line with the current date
                cell["source"][i] = f"**Date last modified: {current_date}**\n"
                break

# Save the updated notebook
with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)