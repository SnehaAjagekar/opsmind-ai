from src.data_analyzer import BusinessDataAnalyzer
from src.gemini_client import ask_gemini


class BusinessAI:

    def __init__(self, csv_path):
        self.analyzer = BusinessDataAnalyzer(csv_path)

    def ask(self, question: str):

        question_lower = question.lower().strip()

        # --------------------------------------------------
        # TOTAL SALES
        # --------------------------------------------------

        if "total sales" in question_lower:

            total_sales = self.analyzer.total_sales()

            return f"Total sales are ₹{total_sales:,.0f}."

        # --------------------------------------------------
        # TOTAL ORDERS
        # --------------------------------------------------

        if (
            "total orders" in question_lower
            or "how many orders" in question_lower
            and "total" in question_lower
        ):

            total_orders = self.analyzer.total_orders()

            return f"The total number of orders is {total_orders}."

        # --------------------------------------------------
        # CANCELLED ORDERS
        # --------------------------------------------------

        if (
            "cancelled" in question_lower
            or "canceled" in question_lower
        ):

            cancelled = self.analyzer.cancelled_orders()

            return f"There are {cancelled} cancelled orders."

        # --------------------------------------------------
        # RETURNED ORDERS
        # --------------------------------------------------

        if "returned" in question_lower:

            returned = self.analyzer.returned_orders()

            return f"There are {returned} returned orders."

        # --------------------------------------------------
        # HIGHEST SALES REGION
        # --------------------------------------------------

        if (
            "highest sales" in question_lower
            and "region" in question_lower
        ):

            sales_by_region = self.analyzer.sales_by_region()

            highest_region = max(
                sales_by_region,
                key=sales_by_region.get
            )

            highest_sales = sales_by_region[highest_region]

            return (
                f"{highest_region} has the highest sales "
                f"with ₹{highest_sales:,.0f}."
            )

        # --------------------------------------------------
        # LOWEST SALES REGION
        # --------------------------------------------------

        if (
            "lowest sales" in question_lower
            and "region" in question_lower
        ):

            sales_by_region = self.analyzer.sales_by_region()

            lowest_region = min(
                sales_by_region,
                key=sales_by_region.get
            )

            lowest_sales = sales_by_region[lowest_region]

            return (
                f"{lowest_region} has the lowest sales "
                f"with ₹{lowest_sales:,.0f}."
            )

        # --------------------------------------------------
        # HIGHEST SALES CATEGORY
        # --------------------------------------------------

        if (
            "highest sales" in question_lower
            and "category" in question_lower
        ):

            sales_by_category = self.analyzer.sales_by_category()

            highest_category = max(
                sales_by_category,
                key=sales_by_category.get
            )

            highest_sales = sales_by_category[highest_category]

            return (
                f"{highest_category} has the highest sales "
                f"with ₹{highest_sales:,.0f}."
            )

        # --------------------------------------------------
        # LOWEST SALES CATEGORY
        # --------------------------------------------------

        if (
            "lowest sales" in question_lower
            and "category" in question_lower
        ):

            sales_by_category = self.analyzer.sales_by_category()

            lowest_category = min(
                sales_by_category,
                key=sales_by_category.get
            )

            lowest_sales = sales_by_category[lowest_category]

            return (
                f"{lowest_category} has the lowest sales "
                f"with ₹{lowest_sales:,.0f}."
            )

        # --------------------------------------------------
        # SALES BY REGION
        # --------------------------------------------------

        if "sales by region" in question_lower:

            sales_by_region = self.analyzer.sales_by_region()

            result = "Sales by region:\n"

            for region, sales in sales_by_region.items():

                result += (
                    f"- {region}: ₹{sales:,.0f}\n"
                )

            return result

        # --------------------------------------------------
        # SALES BY CATEGORY
        # --------------------------------------------------

        if "sales by category" in question_lower:

            sales_by_category = self.analyzer.sales_by_category()

            result = "Sales by category:\n"

            for category, sales in sales_by_category.items():

                result += (
                    f"- {category}: ₹{sales:,.0f}\n"
                )

            return result

        # --------------------------------------------------
        # FALLBACK TO GEMINI
        # --------------------------------------------------

        data = self.analyzer.summary()

        prompt = f"""
You are OpsMind AI, a business analytics assistant.

Answer the user's question using ONLY the
provided business data.

Do not invent numbers.

If the requested information cannot be
determined from the provided business data,
say:

"I could not determine this from the
provided business data."

BUSINESS DATA:

{data}

USER QUESTION:

{question}

Give a clear and concise answer.
"""

        return ask_gemini(prompt)























# import json

# from src.data_analyzer import BusinessDataAnalyzer
# from src.gemini_client import ask_gemini


# class BusinessAI:

#     def __init__(self, csv_path):

#         self.analyzer = BusinessDataAnalyzer(
#             csv_path
#         )


#     def ask(self, question: str):

#         # Get calculated business data
#         data = self.analyzer.summary()

#         # Convert Python dictionary to readable JSON
#         business_data = json.dumps(
#             data,
#             indent=2
#         )

#         prompt = f"""
# You are OpsMind AI, a business analytics assistant.

# Answer the user's question using ONLY the
# provided business data.

# Do not invent numbers.

# If the requested information cannot be
# determined from the provided data, say:

# "I could not determine this from the
# provided business data."

# BUSINESS DATA:

# {business_data}

# USER QUESTION:

# {question}

# Give a clear and concise answer.
# If useful, include the relevant numbers.
# """

#         answer = ask_gemini(prompt)

#         return answer