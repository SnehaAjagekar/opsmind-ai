from src.document_loader import load_document
from src.chunking import split_text
from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore


print("=" * 60)
print("PHASE 6 — FAISS VECTOR STORE TEST")
print("=" * 60)


# --------------------------------------------------
# 1. Load document
# --------------------------------------------------

print("\nLoading document...")

document_path = "src/data/documents/company_policy.txt"

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
# 3. Create embeddings
# --------------------------------------------------

print("\nLoading embedding model...")

embedding_model = EmbeddingModel()

print("\nCreating embeddings...")

embeddings = embedding_model.encode(chunks)

print("✅ Embeddings created.")


# --------------------------------------------------
# 4. Create FAISS vector store
# --------------------------------------------------

print("\nCreating FAISS vector store...")

dimension = embeddings.shape[1]

vector_store = VectorStore(dimension)

print("✅ FAISS vector store created.")


# --------------------------------------------------
# 5. Add documents
# --------------------------------------------------

print("\nAdding documents to FAISS...")

vector_store.add_documents(
    embeddings,
    chunks
)

print("✅ Documents added to FAISS.")

print(
    f"Number of vectors in FAISS: "
    f"{vector_store.index.ntotal}"
)


# --------------------------------------------------
# 6. Create test query
# --------------------------------------------------

question = "How many days do I have to request a refund?"

print("\n" + "=" * 60)
print("SEARCH TEST")
print("=" * 60)

print(f"\nQuestion:")
print(question)


# --------------------------------------------------
# 7. Convert question into embedding
# --------------------------------------------------

print("\nCreating query embedding...")

query_embedding = embedding_model.encode(
    [question]
)[0]

print("✅ Query embedding created.")


# --------------------------------------------------
# 8. Search FAISS
# --------------------------------------------------

print("\nSearching FAISS...")

results = vector_store.search(
    query_embedding,
    top_k=3
)

print("✅ Search completed.")


# --------------------------------------------------
# 9. Display results
# --------------------------------------------------

print("\n" + "=" * 60)
print("TOP SEARCH RESULTS")
print("=" * 60)

for i, result in enumerate(results):

    print(f"\n--- Result {i + 1} ---")

    print(
        f"Distance: "
        f"{result['distance']:.4f}"
    )

    print("\nText:")

    print(result["text"])


# --------------------------------------------------
# 10. Validation
# --------------------------------------------------

if len(results) > 0:

    print("\n" + "=" * 60)
    print("🎉 PHASE 6 COMPLETED SUCCESSFULLY!")
    print("=" * 60)

else:

    raise ValueError(
        "FAISS search returned no results."
    )