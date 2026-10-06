from src.business_ai import BusinessAI


print("=" * 60)
print("PHASE 9 — BUSINESS AI TEST")
print("=" * 60)


# --------------------------------------------------
# 1. Create Business AI
# --------------------------------------------------

csv_path = "src\data\csv\orders.csv"

business_ai = BusinessAI(
    csv_path
)


# --------------------------------------------------
# 2. Test questions
# --------------------------------------------------

questions = [
    "What are the total sales?",
    "Which region has the highest sales?",
    "How many orders were cancelled?",
    "Which product category generated more sales?"
]


# --------------------------------------------------
# 3. Ask Gemini
# --------------------------------------------------

for question in questions:

    print("\n" + "=" * 60)
    print("QUESTION")
    print("=" * 60)

    print(question)

    print("\nSending question to Gemini...")

    answer = business_ai.ask(
        question
    )

    print("\n" + "-" * 60)
    print("GEMINI ANSWER")
    print("-" * 60)

    print(answer)


print("\n" + "=" * 60)
print("🎉 PHASE 9 BUSINESS AI COMPLETED!")
print("=" * 60)