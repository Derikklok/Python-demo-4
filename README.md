# Python Learning Project

A repository for learning Python programming concepts and best practices.

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Git

### Virtual Environment Setup

1. **Create a virtual environment:**
   ```powershell
   python -m venv .venv
   ```

2. **Activate the virtual environment:**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

3. **Deactivate when done:**
   ```powershell
   deactivate
   ```

## 📚 Project Structure

```
Python-demo-4/
├── app.py          # Main application file
├── README.md       # Project documentation
└── .venv/          # Virtual environment (not tracked in git)
```

## 🔧 Git Workflow

### Viewing Available Branches

1. **View all local branches:**
   ```bash
   git branch
   ```

2. **View all remote branches:**
   ```bash
   git branch -r
   ```

3. **View all branches (local and remote):**
   ```bash
   git branch -a
   ```

4. **View branches with last commit info:**
   ```bash
   git branch -v
   ```

### Working with Existing Branches

#### Switching to an Existing Branch

1. **Switch to an existing local branch:**
   ```bash
   git checkout branch-name
   ```

2. **Switch to a remote branch (creates local tracking branch):**
   ```bash
   git checkout -b local-branch-name origin/remote-branch-name
   ```

3. **Quick switch to an existing branch:**
   ```bash
   git switch branch-name
   ```

#### Uploading Content to an Existing Branch

1. **Switch to the target branch:**
   ```bash
   git checkout existing-branch-name
   ```

2. **Pull latest changes from remote:**
   ```bash
   git pull origin existing-branch-name
   ```

3. **Make your changes, then stage them:**
   ```bash
   git add .
   # Or stage specific files
   git add filename.py
   ```

4. **Commit your changes:**
   ```bash
   git commit -m "Your descriptive commit message"
   ```

5. **Push changes to the existing branch:**
   ```bash
   git push origin existing-branch-name
   ```

#### Alternative: Upload to Existing Branch Without Switching

1. **Stay on your current branch and push to different branch:**
   ```bash
   # Make sure you're on the correct branch first
   git status
   
   # If you need to push current changes to a different existing branch
   git push origin HEAD:existing-branch-name
   ```

### Creating a New Feature Branch

1. **Create and switch to a new branch:**
   ```bash
   git checkout -b feature/new-cool-thing
   ```

2. **Make your changes and stage them:**
   ```bash
   git add .
   ```

3. **Commit your changes:**
   ```bash
   git commit -m "Add new cool thing"
   ```

4. **Push the branch to GitHub:**
   ```bash
   git push origin feature/new-cool-thing
   ```

### Updating Main Branch

1. **Switch to main branch:**
   ```bash
   git checkout main
   ```

2. **Pull the latest changes:**
   ```bash
   git pull origin main
   ```

### Useful Branch Commands

1. **Delete a local branch:**
   ```bash
   git branch -d branch-name
   ```

2. **Force delete a local branch:**
   ```bash
   git branch -D branch-name
   ```

3. **Delete a remote branch:**
   ```bash
   git push origin --delete branch-name
   ```

4. **Rename current branch:**
   ```bash
   git branch -m new-branch-name
   ```

5. **Track a remote branch:**
   ```bash
   git branch --set-upstream-to=origin/branch-name
   ```

## 🛠️ Development

### Running the Application

```powershell
# Activate virtual environment first
.\.venv\Scripts\Activate.ps1

# Run the main application
python app.py
```

## 📝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is for educational purposes.