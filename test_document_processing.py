from src.document_loader import load_document
from src.chunking import split_text


# --------------------------------------------------
# 1. Load document
# --------------------------------------------------

document_path = "C:\\Users\\SnehaAj\\OneDrive\\Desktop\\RAG_and_LLMProject\\src\\data\\documents\\company_policy.txt"

print("=" * 60)
print("PHASE 4 — DOCUMENT PROCESSING TEST")
print("=" * 60)

print("\nLoading document...")

text = load_document(document_path)

print("✅ Document loaded successfully.")

print(f"\nTotal characters: {len(text)}")
print(f"Total words: {len(text.split())}")


# --------------------------------------------------
# 2. Split document into chunks
# --------------------------------------------------

print("\nSplitting document into chunks...")

chunks = split_text(
    text,
    chunk_size=500,
    chunk_overlap=100
)

print("✅ Document split successfully.")

print(f"Number of chunks: {len(chunks)}")


# --------------------------------------------------
# 3. Display chunks
# --------------------------------------------------

print("\n" + "=" * 60)
print("GENERATED CHUNKS")
print("=" * 60)

for i, chunk in enumerate(chunks):

    print(f"\n--- Chunk {i + 1} ---")

    print(chunk)

    print(
        f"\nCharacters: {len(chunk)}"
    )


# --------------------------------------------------
# 4. Final verification
# --------------------------------------------------

if len(chunks) > 0:

    print("\n" + "=" * 60)
    print("🎉 PHASE 4 COMPLETED SUCCESSFULLY!")
    print("=" * 60)

else:

    raise ValueError(
        "No chunks were generated."
    )