from pathlib import Path
import pandas as pd


# --------------------------------------------------
# Check policy document
# --------------------------------------------------

document_path = Path(
    "src/data/documents/company_policy.txt"
)

if not document_path.exists():
    raise FileNotFoundError(
        "company_policy.txt was not found."
    )

document_text = document_path.read_text(
    encoding="utf-8"
)

print("=" * 60)
print("DOCUMENT CHECK")
print("=" * 60)

print(f"Document exists: ✅")
print(f"Characters: {len(document_text)}")
print(f"Words: {len(document_text.split())}")

print("\nFirst 300 characters:")
print(document_text[:300])


# --------------------------------------------------
# Check CSV
# --------------------------------------------------

csv_path = Path(
    "src/data/csv/orders.csv"
)

if not csv_path.exists():
    raise FileNotFoundError(
        "orders.csv was not found."
    )

df = pd.read_csv(csv_path)

print("\n" + "=" * 60)
print("CSV CHECK")
print("=" * 60)

print("CSV exists: ✅")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

print("\nColumns:")
print(list(df.columns))

print("\nFirst 5 rows:")
print(df.head())


# --------------------------------------------------
# Basic validation
# --------------------------------------------------

required_columns = [
    "Order_ID",
    "Order_Date",
    "Product",
    "Category",
    "Amount",
    "Status",
    "Customer_Type",
    "Region"
]

missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Missing columns: {missing_columns}"
    )

print("\n" + "=" * 60)
print("DATA VALIDATION")
print("=" * 60)

print("Required columns: ✅")
print("Document: ✅")
print("CSV: ✅")
print("\n🎉 Phase 3 data preparation completed successfully!")