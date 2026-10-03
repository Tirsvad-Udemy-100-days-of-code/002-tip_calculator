# 🚀 Tip Calculator

A beginner-friendly Python console app that splits a restaurant bill, including a tip, between friends.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)

## 🧭 Overview

Day 2 project from Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*. The program asks for the total bill, the tip percentage and the number of people, then prints what each person should pay, rounded to two decimal places.

```
Welcome to the tip calculator!
What was the total bill? $124.56
What percentage tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7
Each person should pay: $19.93
```

## 📋 Requirements

- Python 3.13 or newer
- No runtime dependencies

## 🛠️ Setup

Create and activate a local virtual environment:

```powershell
# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux / Git Bash
python -m venv .venv
source .venv/bin/activate        # Git Bash on Windows: source .venv/Scripts/activate
```

Install the project in editable mode (required to run it from `src/`; also adds the `tip-calculator` command):

```bash
pip install -e .
```

Secrets such as repository tokens belong in a local `.env` file (see `.env.example`). `.env` is git-ignored; the app itself does not need it.

## ▶️ Run

```bash
python -m tip_calculator
```

## 🧪 Tests

```bash
python -m unittest discover -s tests
```

## 📄 License

No license has been chosen yet.

## 🔗 Links

- [Repository](https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/002-tip_calculator)
- [Documentation](https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/002-tip_calculator#readme)
- [Issue tracker](https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/002-tip_calculator/issues)
