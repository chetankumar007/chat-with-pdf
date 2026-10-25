
from pypdf import PdfReader


def extract_pdf_text(file_path: str) -> list[dict]:
    reader = PdfReader(file_path)
    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        if text.strip():
            pages.append({
                "page": page_number,
                "text": text.strip()
            })

    return pages


if __name__ == "__main__":
    pages = extract_pdf_text("sample.pdf")

    print(f"Extracted text from {len(pages)} pages.\n")

    for page in pages:
        print(f"--- Page {page['page']} ---")
        print(page["text"])
        print()
