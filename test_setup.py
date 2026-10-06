"""
OpsMind AI - Setup Verification Script (Phase 1)

Checks the environment, Python version, and major dependencies:
- Official Google GenAI SDK (`google-genai`)
- Streamlit
- Pandas
- PyPDF
- Sentence Transformers
- FAISS
- LangChain text splitters
- Python-dotenv

Note: This script verifies local installations and does NOT require or call the Gemini API.
"""

import sys

def check_environment():
    print("=" * 60)
    print("OpsMind AI — Environment & Dependency Check")
    print("=" * 60)
    
    # 1. Python Version Check
    py_version = sys.version.split()[0]
    print(f"\n[Python Version]: {py_version}")
    if sys.version_info < (3, 10):
        print("  ❌ WARNING: Python 3.10+ is recommended.")
    else:
        print("  ✅ Python version is compatible.")

    modules_to_check = [
        ("google.genai", "Google GenAI SDK (Official modern SDK)", None),
        ("streamlit", "Streamlit UI Framework", "__version__"),
        ("pandas", "Pandas Data Analysis", "__version__"),
        ("pypdf", "PyPDF Document Processing", "__version__"),
        ("sentence_transformers", "Sentence Transformers (Embeddings)", "__version__"),
        ("faiss", "FAISS Vector Search Engine", None),
        ("langchain_text_splitters", "LangChain Text Splitters", None),
        ("dotenv", "Python Dotenv (Environment Loader)", "__version__"),
    ]

    print("\n[Checking Core Dependencies]:")
    all_passed = True

    for mod_name, description, ver_attr in modules_to_check:
        try:
            mod = __import__(mod_name, fromlist=["*"])
            ver_str = ""
            if ver_attr and hasattr(mod, ver_attr):
                ver_str = f" (v{getattr(mod, ver_attr)})"
            elif mod_name == "faiss":
                ver_str = " (FAISS CPU ready)"
            elif mod_name == "google.genai":
                # Check for modern client class existence
                if hasattr(mod, "Client"):
                    ver_str = " (Client available)"
            print(f"  ✅ {description} ({mod_name}){ver_str}")
        except Exception as e:
            print(f"  ❌ Failed to import {mod_name} ({description}): {e}")
            all_passed = False

    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 All Phase 1 environment & dependency checks PASSED!")
        print("=" * 60)
        return 0
    else:
        print("⚠️ Some dependency checks failed. Please see above errors.")
        print("=" * 60)
        return 1

if __name__ == "__main__":
    sys.exit(check_environment())
