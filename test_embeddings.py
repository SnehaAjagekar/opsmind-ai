from src.document_loader import load_document
from src.chunking import split_text
from src.embeddings import EmbeddingModel


# --------------------------------------------------
# 1. Load document
# --------------------------------------------------

document_path = "src/data/documents/company_policy.txt"

print("=" * 60)
print("PHASE 5 — EMBEDDING TEST")
print("=" * 60)

print("\nLoading document...")

text = load_document(document_path)

print("✅ Document loaded.")


# --------------------------------------------------
# 2. Create chunks
# --------------------------------------------------

print("\nCreating chunks...")

chunks = split_text(
    text,
    chunk_size=500,
    chunk_overlap=100
)

print(f"✅ Created {len(chunks)} chunks.")


# --------------------------------------------------
# 3. Load embedding model
# --------------------------------------------------

print("\nLoading embedding model...")

embedding_model = EmbeddingModel()


# --------------------------------------------------
# 4. Create embeddings
# --------------------------------------------------

print("\nCreating embeddings...")

embeddings = embedding_model.encode(chunks)

print("✅ Embeddings created.")


# --------------------------------------------------
# 5. Display information
# --------------------------------------------------

print("\n" + "=" * 60)
print("EMBEDDING INFORMATION")
print("=" * 60)

print(f"Number of chunks: {len(chunks)}")

print(
    f"Embedding matrix shape: {embeddings.shape}"
)

print(
    f"Embedding vector size: {embeddings.shape[1]}"
)


# --------------------------------------------------
# 6. Display first vector
# --------------------------------------------------

print("\nFirst chunk:")

print(chunks[0])

print("\nFirst embedding vector:")

print(embeddings[0])

print("\nFirst vector length:")

print(len(embeddings[0]))


# --------------------------------------------------
# 7. Final validation
# --------------------------------------------------

if len(embeddings) == len(chunks):

    print("\n" + "=" * 60)
    print("🎉 PHASE 5 COMPLETED SUCCESSFULLY!")
    print("=" * 60)

else:

    raise ValueError(
        "Number of embeddings does not match number of chunks."
    )