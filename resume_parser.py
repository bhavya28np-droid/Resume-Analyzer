"""
Resume file handling and text extraction.
"""

from pathlib import Path


def extract_text_from_file(file_path):
    """Extract text from TXT or PDF resume files."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError("The selected resume file does not exist.")

    if path.suffix.lower() == ".txt":
        return path.read_text(encoding="utf-8", errors="ignore")

    if path.suffix.lower() == ".pdf":
        try:
            from pypdf import PdfReader
        except ImportError:
            raise ImportError(
                "PDF support requires pypdf. Install it with: pip install pypdf"
            )

        reader = PdfReader(str(path))
        pages = []

        for page in reader.pages:
            pages.append(page.extract_text() or "")

        return "\n".join(pages)

    raise ValueError("Unsupported file type. Please select a PDF or TXT file.")
