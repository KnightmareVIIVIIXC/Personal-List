#!/bin/bash

# Enter the path to your local repository
REPO_PATH="C:/Users/Logan/Documents/GitHub/phishfort-lists"

# Enter your GitHub username
USERNAME="KnightmareVIIVIIXC"

# Enter the name of the repository on GitHub
REPO_NAME="phishfort-lists"

# Enter the commit message
COMMIT_MSG="update"

# Change directory to your local repository
cd "$REPO_PATH"

# Add all changes to the staging area
git add .

# Commit the changes with the given commit message
git commit -m "$COMMIT_MSG"

# Push the changes to GitHub
git push "https://github.com/$USERNAME/$REPO_NAME.git"
