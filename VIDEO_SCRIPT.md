# Video Explanation Guide

1. Explain that one person is simulating two developers with two branches and
   two local working folders.
2. Show Developer A initializing the repository and pushing the initial `main`.
3. Show Developer A creating `developer-a-setup`, adding the base application,
   pushing the branch, and merging it into `main`.
4. Explain that the remote repository is the shared GitHub copy of the project.
5. Show `git clone` creating Developer B's independent local copy.
6. Show Developer B running `git fetch` and creating
   `developer-b-contact-search` from `origin/main`.
7. Show Developer B adding contact search, running tests, reviewing `git diff`,
   committing, and pushing the branch.
8. Show the Pull Request and explain that it proposes merging Developer B's
   branch into `main` without changing `main` immediately.
9. As Developer A, run `git fetch`, inspect remote branches and commits, review
   the Pull Request diff, run its tests, and leave a review comment.
10. Merge the Pull Request and explain the merge commit.
11. Run `git pull` in Developer A's folder to update local `main`, then show
    Developer B fetching and pulling the same final `main` branch.
12. Run the final tests and application, then show `git log --graph`.
13. Explain the difference between fetch and pull:
    `fetch` downloads remote information; `pull` downloads and integrates it into
    the current branch.
14. Copy the public repository and Pull Request URLs into the assignment form.
