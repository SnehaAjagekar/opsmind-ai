from src.rag_pipeline import RAGPipeline


print("=" * 60)
print("PHASE 7 — RAG PIPELINE TEST")
print("=" * 60)


# --------------------------------------------------
# 1. Create RAG pipeline
# --------------------------------------------------

document_path = "src/data/documents/company_policy.txt"

rag = RAGPipeline(
    document_path
)


# --------------------------------------------------
# 2. Test questions
# --------------------------------------------------

questions = [
    "How many days do I have to request a refund?",
    "What should I do if my product arrives damaged?",
    "Can I cancel an order after it has been shipped?",
    "How long does standard delivery take?"
]


# --------------------------------------------------
# 3. Ask questions
# --------------------------------------------------

for question in questions:

    print("\n" + "=" * 60)
    print("QUESTION")
    print("=" * 60)

    print(question)

    result = rag.ask(question)


    # --------------------------------------------------
    # 4. Display Gemini answer
    # --------------------------------------------------

    print("\n" + "-" * 60)
    print("GEMINI ANSWER")
    print("-" * 60)

    print(result["answer"])


    # --------------------------------------------------
    # 5. Display retrieved sources
    # --------------------------------------------------

    print("\n" + "-" * 60)
    print("RETRIEVED SOURCES")
    print("-" * 60)

    for i, source in enumerate(
        result["sources"]
    ):

        print(
            f"\nSource {i + 1} "
            f"(distance: "
            f"{source['distance']:.4f})"
        )

        print(source["text"])


print("\n" + "=" * 60)
print("🎉 PHASE 7 RAG TEST COMPLETED!")
print("=" * 60)
