# Multi-Developer GitHub Simulation

This project simulates two developers collaborating on a Python Contact Book
through Git and GitHub.

## Scenario

### Developer A

1. Creates the initial Contact Book project.
2. Initializes a local Git repository.
3. Creates the public GitHub repository and pushes the initial `main` branch.
4. Creates and works on the `developer-a-setup` branch.
5. Pushes and merges that branch into `main`.

### Developer B

1. Clones Developer A's public repository.
2. Creates the `developer-b-contact-search` branch.
3. Implements case-insensitive contact search.
4. Updates the demonstration and tests.
5. Commits and pushes the feature branch.
6. Creates a Pull Request into `main`.

### Review and merge

Developer A fetches the remote changes, reviews the Pull Request diff, leaves a
review comment, merges the Pull Request, and pulls the updated `main` branch.
Developer B then fetches and pulls the completed `main` branch into the cloned
workspace.

## Branches used for the simulation

| Branch | Simulated owner | Purpose |
|---|---|---|
| `developer-a-setup` | Developer A | Adds the initial Contact Book application. |
| `developer-b-contact-search` | Developer B | Adds contact-search functionality and tests. |
| `main` | Shared | Receives the completed work from both developers. |

## Project structure

```text
6_multi_developer_github_simulation/
├── .gitignore
├── README.md
├── VIDEO_SCRIPT.md
├── contact.py
├── contact_book.py
├── logging_config.py
├── main.py
├── test_contact_book.py
├── git_workflow.sh
└── .developer_b_seed/
    ├── contact_book.py
    ├── main.py
    └── test_contact_book.py
```

`.developer_b_seed/` contains Developer B's prepared feature changes. It is ignored
by Git. The workflow script copies those files into Developer B's cloned repository
so the feature appears only on the feature branch.

## Application features

- Create validated contacts.
- Reject duplicate email addresses.
- List contacts without exposing the internal mutable list.
- Search by a case-insensitive name or email fragment after Developer B's feature.
- Log application activity to `logs/contact_book.log`.

## Run the initial Developer A version

```bash
python main.py
python test_contact_book.py
```

## Git and GitHub workflow

Open `git_workflow.sh` and copy its commands into the terminal one block at a
time while recording. Do not run the complete file automatically because you
need to explain each developer's actions.

```bash
cd /Users/JJOHN41/Documents/my_learning/euron_super30/assignment/week6/6_multi_developer_github_simulation
```

The script demonstrates:

- `git init`
- `git clone`
- `git remote`
- `git fetch`
- `git pull`
- `git push`
- Two developer branches
- Meaningful commits
- Pull Request creation
- Pull Request diff review and review comment
- Pull Request merge
- Final Git history

The commands require GitHub CLI to be installed and authenticated. Because one
GitHub account normally cannot approve its own Pull Request, Developer A records
the review using a Pull Request comment before merging.

## Submission links

- Public GitHub repository: `GENERATED-AFTER-RUNNING-THE-SCRIPT`
- Pull Request: `GENERATED-AFTER-RUNNING-THE-SCRIPT`
- YouTube video: `ADD-YOUTUBE-VIDEO-URL`
