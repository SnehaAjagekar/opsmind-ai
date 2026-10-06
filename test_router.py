from src.router import OpsMindRouter


print("=" * 60)
print("PHASE 11 — OPSMIND AI ROUTER TEST")
print("=" * 60)



document_path = "src/data/documents/company_policy.txt"

csv_path = "src/data/csv/orders.csv"


# --------------------------------------------------
# Create router
# --------------------------------------------------

router = OpsMindRouter(
    document_path,
    csv_path
)


# --------------------------------------------------
# Test questions
# --------------------------------------------------

questions = [

    "What is the refund policy?",

    "What should I do if I receive a damaged product?",

    "Which region has the highest sales?",

    "What are the total sales?",

    "How many orders were cancelled?"

]


# --------------------------------------------------
# Ask questions
# --------------------------------------------------

for question in questions:

    print("\n" + "=" * 60)

    print("QUESTION:")
    print(question)

    result = router.ask(
        question
    )

    print("\nROUTE:")
    print(result["route"])

    print("\nANSWER:")
    print(result["answer"])


print("\n" + "=" * 60)
print("🎉 PHASE 11 ROUTER TEST COMPLETED!")
print("=" * 60)