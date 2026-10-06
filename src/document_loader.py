from pathlib import Path
from pypdf import PdfReader


def load_text_file(file_path: str) -> str:
    """
    Load text from a TXT file.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    return path.read_text(
        encoding="utf-8"
    )


def load_pdf(file_path: str) -> str:
    """
    Extract text from a PDF file.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    reader = PdfReader(str(path))

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def load_document(file_path: str) -> str:
    """
    Load either TXT or PDF document.
    """

    if file_path.endswith(".txt"):
        return load_text_file(file_path)

    elif file_path.endswith(".pdf"):
        return load_pdf(file_path)

    else:
        raise ValueError(
            "Only .txt and .pdf files are supported."
        )