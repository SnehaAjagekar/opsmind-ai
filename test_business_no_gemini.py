from src.business_ai import BusinessAI



csv_path = "src/data/csv/orders.csv"

business_ai = BusinessAI(csv_path)


questions = [
    "What are the total sales?",
    "Which region has the highest sales?",
    "How many total orders are there?",
    "How many orders were cancelled?",
    "How many orders were returned?",
    "Which category has the highest sales?"
]


for question in questions:

    print("=" * 60)

    print("QUESTION:")
    print(question)

    answer = business_ai.ask(question)

    print("\nANSWER:")
    print(answer)

    print()