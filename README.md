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