
from sentence_transformers import SentenceTransformer

from read_pdf import extract_pdf_text
from chunk_text import chunk_pages


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def embed_chunks(chunks: list[dict]):
    model = SentenceTransformer(MODEL_NAME)

    texts = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(
        texts,
        normalize_embeddings=True,
        show_progress_bar=True,
    )

    return embeddings


if __name__ == "__main__":
    pages = extract_pdf_text("sample.pdf")
    chunks = chunk_pages(pages)

    if not chunks:
        raise ValueError("No text found in the PDF.")

    embeddings = embed_chunks(chunks)

    print(f"\nChunks: {len(chunks)}")
    print(f"Embedding shape: {embeddings.shape}")
    print(f"\nFirst chunk embedding (first 10 values):")
    print(embeddings[0][:10])
