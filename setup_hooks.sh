#!/bin/bash
# Create the pre-commit hook if it doesn't exist
if [ ! -f .git/hooks/pre-commit ]; then
    cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
./ipynb_to_md.sh
git add **/*.md
EOF
    chmod +x .git/hooks/pre-commit
    echo "Git hook set up successfully."
else
    echo "Git hook already exists."
fi
