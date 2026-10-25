
def chunk_pages(
    pages: list[dict],
    chunk_size: int = 1000,
    overlap: int = 150,
) -> list[dict]:
    """Split extracted PDF pages into overlapping text chunks."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be >= 0 and smaller than chunk_size")

    chunks = []
    step = chunk_size - overlap

    for page in pages:
        text = page["text"]
        page_number = page["page"]

        for start in range(0, len(text), step):
            chunk_text = text[start : start + chunk_size].strip()

            if chunk_text:
                chunks.append({
                    "page": page_number,
                    "text": chunk_text,
                })

    return chunks


if __name__ == "__main__":
    from read_pdf import extract_pdf_text

    pages = extract_pdf_text("sample.pdf")
    chunks = chunk_pages(pages)

    print(f"Pages: {len(pages)}")
    print(f"Chunks: {len(chunks)}")

    for index, chunk in enumerate(chunks[:3], start=1):
        print(f"\n--- Chunk {index} | Page {chunk['page']} ---")
        print(chunk["text"][:300])
