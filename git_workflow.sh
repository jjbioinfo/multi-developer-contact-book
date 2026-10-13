#!/usr/bin/env bash

# Copy and run these commands one block at a time while recording the video.
# Do not run the complete file automatically.

# Store the repository name and the paths representing both developers.
REPOSITORY_NAME="multi-developer-contact-book"
DEVELOPER_A_DIR=$(pwd)
DEVELOPER_B_DIR="${DEVELOPER_A_DIR}_developer_b_clone"
FEATURE_SOURCE="$DEVELOPER_A_DIR/.developer_b_seed"

# Confirm that Git and GitHub CLI are available and GitHub CLI is authenticated.
command -v git
command -v gh
gh auth status

# Developer A initializes the repository and uses a separate local identity. 
git init -b main
git config user.name "jjbioinfo"
git config user.email "jibinbioinfo@gmail.com"

# Developer A creates the initial main commit containing the project setup.
git add .gitignore README.md VIDEO_SCRIPT.md git_workflow.sh logging_config.py
git commit -m "Set up multi-developer Contact Book project"

# Developer A creates the public remote repository and pushes main.  
gh repo create "$REPOSITORY_NAME" --public --source=. --remote=origin
git remote -v
git push -u origin main
REPOSITORY_URL=$(gh repo view --json url --jq .url)

# Developer A creates the first developer branch and implements the base project.
git switch -c developer-a-setup
git add contact.py contact_book.py main.py test_contact_book.py
git commit -m "Add initial Contact Book application"
python test_contact_book.py
git push -u origin developer-a-setup

# Developer A merges the first developer branch into main and pushes it.
git switch main
git merge --no-ff developer-a-setup -m "Merge Developer A project setup"
git push origin main

# Developer B creates an independent local workspace by cloning the repository.
git clone "$REPOSITORY_URL" "$DEVELOPER_B_DIR"
cd "$DEVELOPER_B_DIR"
git config user.name "Developer B"
git config user.email "developer.b@example.com"
git remote -v

# Developer B fetches remote information before starting new work.
git fetch origin
git branch --all

# Developer B creates the second developer branch from the latest remote main.
git switch -c developer-b-contact-search origin/main

# Developer B implements the contact-search feature using the prepared files.
cp "$FEATURE_SOURCE/contact_book.py" contact_book.py
cp "$FEATURE_SOURCE/main.py" main.py
cp "$FEATURE_SOURCE/test_contact_book.py" test_contact_book.py
git status
git diff
python test_contact_book.py

# Developer B commits and pushes the second developer branch.
git add contact_book.py main.py test_contact_book.py
git commit -m "Add contact search feature"
git push -u origin developer-b-contact-search

# Developer B creates a Pull Request from the feature branch into main.
PR_URL=$(gh pr create \
    --base main \
    --head developer-b-contact-search \
    --title "Add contact search feature" \
    --body "Developer B adds case-insensitive contact search and its tests.")

# Developer A returns to the original workspace and fetches Developer B's branch.
cd "$DEVELOPER_A_DIR"
git fetch origin
git branch --all

# Developer A reviews the commits, file differences, and Pull Request.
git log --oneline main..origin/developer-b-contact-search
git diff main..origin/developer-b-contact-search
gh pr view "$PR_URL"
gh pr diff "$PR_URL"

# Developer A temporarily checks out the remote branch and runs its tests.
git switch --detach origin/developer-b-contact-search
python test_contact_book.py
git switch main

# With one GitHub account, use a review comment because self-approval is blocked.
gh pr comment "$PR_URL" \
    --body "Developer A reviewed the feature and tests. It is ready to merge."

# Developer A merges the Pull Request and deletes its remote feature branch.
gh pr merge "$PR_URL" --merge --delete-branch

# Developer A pulls the merged main branch and validates the final application.
git switch main
git pull --ff-only origin main
python test_contact_book.py
python main.py

# Save the repository and Pull Request URLs for assignment submission.
printf '# Submission Links\n\n- Repository: %s\n- Pull Request: %s\n' \
    "$REPOSITORY_URL" "$PR_URL" > SUBMISSION_LINKS.md
git add SUBMISSION_LINKS.md
git commit -m "Add repository and Pull Request links"
git push origin main

# Developer B fetches and pulls the final merged main branch. 
cd "$DEVELOPER_B_DIR"
git fetch --prune origin
git switch main
git pull --ff-only origin main

# Display the remote connection and final shared Git history.
git remote -v
git log --oneline --graph --all --decorate
git status

# Display both submission URLs again for copying into the submission form.
gh repo view --json url --jq .url
gh pr view "$PR_URL" --json url --jq .url
