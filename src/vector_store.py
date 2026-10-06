import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension: int):
        """
        Create a FAISS vector index.
        """

        self.dimension = dimension

        # FAISS index using Euclidean distance
        self.index = faiss.IndexFlatL2(dimension)

        # Store original text chunks
        self.documents = []


    def add_documents(self, embeddings, documents):
        """
        Add embeddings and their corresponding
        text documents to the FAISS index.
        """

        embeddings = np.array(
            embeddings
        ).astype("float32")

        self.index.add(embeddings)

        self.documents.extend(documents)


    def search(self, query_embedding, top_k=3):
        """
        Search for the most similar documents.
        """

        query_embedding = np.array(
            [query_embedding]
        ).astype("float32")

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for distance, index in zip(
            distances[0],
            indices[0]
        ):

            if index < len(self.documents):

                results.append({
                    "text": self.documents[index],
                    "distance": float(distance)
                })

        return results