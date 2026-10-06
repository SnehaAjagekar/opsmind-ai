from src.data_analyzer import BusinessDataAnalyzer


print("=" * 60)
print("PHASE 8 — BUSINESS DATA ANALYTICS TEST")
print("=" * 60)


csv_path = "src\data\csv\orders.csv"


# --------------------------------------------------
# 1. Load analyzer
# --------------------------------------------------

print("\nLoading business data...")

analyzer = BusinessDataAnalyzer(
    csv_path
)

print("✅ Business data loaded.")


# --------------------------------------------------
# 2. Calculate metrics
# --------------------------------------------------

print("\nCalculating business metrics...")

total_sales = analyzer.total_sales()
total_orders = analyzer.total_orders()
cancelled = analyzer.cancelled_orders()
returned = analyzer.returned_orders()

print("✅ Metrics calculated.")


# --------------------------------------------------
# 3. Display metrics
# --------------------------------------------------

print("\n" + "=" * 60)
print("BUSINESS METRICS")
print("=" * 60)

print(
    f"\nTotal Sales: ₹{total_sales:,.0f}"
)

print(
    f"Total Orders: {total_orders}"
)

print(
    f"Cancelled Orders: {cancelled}"
)

print(
    f"Returned Orders: {returned}"
)


# --------------------------------------------------
# 4. Category sales
# --------------------------------------------------

print("\n" + "=" * 60)
print("SALES BY CATEGORY")
print("=" * 60)

category_sales = analyzer.sales_by_category()

for category, amount in category_sales.items():

    print(
        f"{category}: ₹{amount:,.0f}"
    )


# --------------------------------------------------
# 5. Region sales
# --------------------------------------------------

print("\n" + "=" * 60)
print("SALES BY REGION")
print("=" * 60)

region_sales = analyzer.sales_by_region()

for region, amount in region_sales.items():

    print(
        f"{region}: ₹{amount:,.0f}"
    )


# --------------------------------------------------
# 6. Complete summary
# --------------------------------------------------

print("\n" + "=" * 60)
print("COMPLETE BUSINESS SUMMARY")
print("=" * 60)

print(
    analyzer.summary()
)


print("\n" + "=" * 60)
print("🎉 PHASE 8 DATA ANALYTICS COMPLETED!")
print("=" * 60)