from src.gemini_client import ask_gemini


def main():

    prompt = """
    Explain what RAG is in very simple language.
    Give the answer in exactly 3 sentences.
    """

    print("\nSending request to Gemini...")
    print("-" * 60)

    answer = ask_gemini(prompt)

    print("Gemini Response:")
    print(answer)

    print("-" * 60)
    print("Gemini API test completed successfully!")


if __name__ == "__main__":
    main()