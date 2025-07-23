# 🧠 Final Programming Project – File Handling System

This project is a custom Python file handling system that demonstrates advanced Object-Oriented Programming (OOP) concepts and real-world file operations.

## ✅ Features

- 🔄 Generator to read large files line-by-line
- 🧠 List comprehension to extract words from files
- ➕ Overloaded `+` operator to combine two files
- 🎨 Custom decorator with ANSI terminal colors (no external libraries)
- 👶 Inheritance and method overriding via `ChildClass`
- 📁 Method to combine multiple files at once
- 🧪 Automated tests using `pytest`
- ☁️ Continuous Integration via GitHub Actions
- 🧰 Makefile and requirements.txt for easy setup

---

## 📁 Project Structure

```
project/
├── MainClass.py
├── ChildClass.py
├── requirements.txt
├── Makefile
├── README.md
├── file1.txt
├── file2.txt
├── combined.txt
├── files_combined.txt
├── tests/
│   └── test_main.py
└── .github/
    └── workflows/
        └── python-app.yml
```

---

## ⚙️ Setup Instructions

### 1. ✅ Install Python (if not already)
Download from: https://www.python.org/downloads/

Make sure you add Python to PATH during installation.

### 2. ✅ Create a Virtual Environment

```bash
cd path/to/project
python -m venv .venv
```

### 3. ✅ Activate the Environment

- **Windows PowerShell**:
```bash
.venv\Scripts\Activate.ps1
```

- **Command Prompt**:
```bash
.venv\Scripts\activate.bat
```

### 4. ✅ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. ✅ Run the Code (Manual Use)

```python
from MainClass import MainClass
from ChildClass import ChildClass

file1 = MainClass("file1.txt")
file2 = MainClass("file2.txt")

# Read lines one at a time
for line in file1.read_lines():
    print(line)

# Read all words as a list
print(file1.read_words_as_list())

# Combine two files using + operator
combined = file1 + file2

# Combine multiple files using child class
child = ChildClass("file1.txt")
multi = child.concat_many_files("file1.txt", "file2.txt")
```

---

## 🧪 Run the Tests

Make sure your virtual environment is activated, then run:

```bash
pytest
```

Expected output:
```
tests/test_main.py .. [100%]
```

---

## 📦 Run Using Makefile

```bash
make test   # Runs pytest
```

---

## ☁️ GitHub CI

Push your code to GitHub and GitHub Actions will run your tests automatically using the `.github/workflows/python-app.yml` config.

---

## 📖 Real-World Use Cases

- Merging logs (e.g., `monday.txt`, `tuesday.txt`, etc.)
- Combining survey responses
- Processing large datasets line-by-line
- Automating weekly reports from daily logs

---

## 👥 Authors

- Team: MiQDAD, Jwan, and friends 🧠
- Date: July 2025

---

## 💬 For Presentation

> “Our project helps automate real-world file processing. It uses efficient reading, custom operators, and decorators — all tested and CI-enabled. It’s like a toolkit for dealing with everyday text files in a clean, reusable way.”