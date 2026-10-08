# Resume Analyzer

A Python-based Resume Analyzer developed as a Python Mini Project.

## Project Information

- **Project No.:** 37
- **Project Title:** Resume Analyzer
- **Major Python Concepts:** Strings, Regex, File Handling
- **Language:** Python
- **GUI:** Tkinter

## Features

- Upload PDF or TXT resumes
- Extract resume text
- Detect email addresses using Regular Expressions
- Detect Indian phone numbers using Regular Expressions
- Identify technical skills
- Calculate a basic resume score
- Display an analysis report through a GUI

## Technologies Used

- Python
- Tkinter
- Regular Expressions (`re`)
- File Handling
- pypdf

## How to Run

1. Install Python.
2. Open the project folder in VS Code.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run:

```bash
python main.py
```

## Project Structure

```text
Resume-Analyzer/
├── main.py
├── analyzer.py
├── resume_parser.py
├── skills.json
├── requirements.txt
├── README.md
├── reports/
└── screenshots/
```

## Future Improvements

- Job-role based skill matching
- Resume improvement suggestions
- Exportable analysis reports
- Better GUI design
- More resume formats
