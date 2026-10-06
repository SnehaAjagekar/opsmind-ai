from src.document_loader import load_document
from src.chunking import split_text
from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore
from src.gemini_client import ask_gemini


class RAGPipeline:

    def __init__(self, document_path):

        print("Loading document...")

        text = load_document(document_path)

        print("Splitting document...")

        self.chunks = split_text(
            text,
            chunk_size=500,
            chunk_overlap=100
        )

        print(
            f"Created {len(self.chunks)} chunks."
        )

        print("Loading embedding model...")

        self.embedding_model = EmbeddingModel()

        print("Creating embeddings...")

        embeddings = self.embedding_model.encode(
            self.chunks
        )

        dimension = embeddings.shape[1]

        print("Creating FAISS vector store...")

        self.vector_store = VectorStore(
            dimension
        )

        self.vector_store.add_documents(
            embeddings,
            self.chunks
        )

        print("RAG pipeline ready!")


    def ask(self, question: str):

        # ------------------------------------------
        # 1. Convert question into embedding
        # ------------------------------------------

        question_embedding = (
            self.embedding_model.encode(
                [question]
            )[0]
        )


        # ------------------------------------------
        # 2. Search relevant chunks
        # ------------------------------------------

        results = self.vector_store.search(
            question_embedding,
            top_k=3
        )


        # ------------------------------------------
        # 3. Create context
        # ------------------------------------------

        context = "\n\n".join(
            result["text"]
            for result in results
        )


        # ------------------------------------------
        # 4. Send context + question to Gemini
        # ------------------------------------------

        prompt = f"""
You are OpsMind AI, a business assistant.

Answer the user's question using ONLY the
provided business information.

If the answer is not available in the
business information, say:

"I could not find this information in the
provided business documents."

Do not invent policies or information.

BUSINESS INFORMATION:

{context}

USER QUESTION:

{question}

Give a clear and concise answer.
"""


        answer = ask_gemini(prompt)


        # ------------------------------------------
        # 5. Return answer + sources
        # ------------------------------------------

        return {
            "answer": answer,
            "sources": results
        }