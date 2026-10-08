"""
Resume analysis logic.

This module demonstrates:
- Strings
- Regular Expressions
- Dictionaries and Lists
- Basic file-independent text processing
"""

import re


SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "SQL",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Node.js",
    "Django",
    "Flask",
    "Git",
    "GitHub",
    "MySQL",
    "MongoDB",
    "Excel",
    "Power BI",
    "Machine Learning",
    "Data Analysis",
    "REST API",
    "AWS",
    "Azure",
    "Docker",
]


def normalize_text(text):
    """Normalize resume text for reliable matching."""
    text = text.replace("\u00a0", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_email(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    match = re.search(pattern, text)
    return match.group(0) if match else "Not found"


def extract_phone(text):
    pattern = r"(?:\+91[-\s]?)?[6-9]\d{9}\b"
    match = re.search(pattern, text)
    return match.group(0) if match else "Not found"


def find_skills(text):
    """Find known skills in resume text."""
    found = []
    lower_text = text.lower()

    for skill in SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text, re.IGNORECASE):
            found.append(skill)

    return found


def calculate_score(text, skills, email, phone):
    """Calculate a simple transparent resume score out of 100."""

    score = 0
    text_lower = text.lower()

    # 1. Contact information - 30 points
    if email != "Not found":
        score += 15

    if phone != "Not found":
        score += 15

    # 2. Technical skills - 30 points
    score += min(len(skills) * 3, 30)

    # 3. Resume sections - 30 points
    sections = {
        "Education": r"\beducation\b",
        "Skills": r"\bskills?\b",
        "Projects": r"\bprojects?\b",
        "Experience": r"\bexperience\b",
        "Certifications": r"\bcertifications?\b",
        "Achievements": r"\bachievements?\b"
    }

    sections_found = 0

    for pattern in sections.values():
        if re.search(pattern, text_lower):
            sections_found += 1

    score += sections_found * 5

    # 4. Resume length - 10 points
    word_count = len(text.split())

    if word_count >= 150:
        score += 10
    elif word_count >= 75:
        score += 5

    return min(score, 100)


def analyze_resume(raw_text):
    """Return a human-readable resume analysis report."""
    text = normalize_text(raw_text)

    email = extract_email(text)
    phone = extract_phone(text)
    skills = find_skills(text)
    score = calculate_score(text, skills, email, phone)
    sections = {
        "Education": r"\beducation\b",
        "Skills": r"\bskills?\b",
        "Projects": r"\bprojects?\b",
        "Experience": r"\bexperience\b",
        "Certifications": r"\bcertifications?\b",
        "Achievements": r"\bachievements?\b"
    }

    detected_sections = []

    for section, pattern in sections.items():
        if re.search(pattern, text, re.IGNORECASE):
            detected_sections.append(section)

    report = []
    report.append("=" * 55)
    report.append("                 RESUME ANALYSIS")
    report.append("=" * 55)
    report.append("")
    report.append(f"Resume word count : {len(text.split())}")
    report.append(f"Email             : {email}")
    report.append(f"Phone             : {phone}")
    report.append("")
    report.append("Skills detected:")
    report.append("- " + (", ".join(skills) if skills else "No listed skills detected"))
    
    report.append("")
    report.append("Resume Sections:")

    for section in sections:
        if section in detected_sections:
            report.append(f"✓ {section}")
        else:
            report.append(f"✗ {section}")
    report.append("")
    report.append(f"Resume Score       : {score}/100")
    report.append("")

    if score >= 80:
        report.append("Overall feedback   : Strong resume structure.")
    elif score >= 60:
        report.append("Overall feedback   : Good start, but some areas can be improved.")
    else:
        report.append("Overall feedback   : Consider adding more relevant details and skills.")

    report.append("")
    report.append("Detected using Python Strings, Regex and File Handling.")
    report.append("=" * 55)

    return "\n".join(report)
