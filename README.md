# solar-challenge-week1

## Project Overview

This repository contains solutions for the Solar Data Discovery Challenge (Week 1), focused on analyzing solar farm data from Benin, Sierra Leone, and Togo. The project covers environment setup, data profiling, cleaning, exploratory data analysis (EDA), and a cross-country comparison, with an optional Streamlit dashboard.

---

## Folder Structure (Recommended)

```
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
├── notebooks/
│   ├── __init__.py
│   └── <country>_eda.ipynb
├── data/           # (ignored in git)
├── tests/
│   ├── __init__.py
├── scripts/
│   ├── __init__.py
│   └── README.md
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
```

---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/samuels5/solar-challenge-week1.git
cd solar-challenge-week1
```

### 2. Create and Activate a Virtual Environment

```sh
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

---

## Development Workflow

- All data files (e.g., CSVs) must be placed in the `data/` folder, which is git-ignored.
- Use feature branches for each major task (e.g., `setup-task`, `eda-benin`, `compare-countries`, `dashboard-dev`).
- Commit frequently with clear, conventional messages (e.g., `init: add .gitignore`).
- Open Pull Requests to merge changes into `main`.

---

## Continuous Integration (CI)

This project uses GitHub Actions for CI. The workflow installs dependencies and checks the Python version on every push or pull request. See `.github/workflows/ci.yml` for details.

---

## How to Reproduce the Environment

1. Clone the repo and navigate to the directory.
2. Create and activate a virtual environment.
3. Install dependencies from `requirements.txt`.

---

## Useful Commands

- Activate venv (Windows):
  ```sh
  .\venv\Scripts\activate
  ```
- Deactivate venv:
  ```sh
  deactivate
  ```
- Install new package:
  ```sh
  pip install <package-name>
  pip freeze > requirements.txt
  ```

---

## Project Tasks

- **Task 1:** Git & Environment Setup
- **Task 2:** Data Profiling, Cleaning & EDA
- **Task 3:** Cross-Country Comparison
- **Bonus:** Streamlit Dashboard

See the challenge instructions for detailed task breakdowns.

---

## References

- [Python Testing](https://realpython.com/python-testing/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)

---

