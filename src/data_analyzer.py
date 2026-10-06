import pandas as pd


class BusinessDataAnalyzer:

    def __init__(self, csv_path):

        self.df = pd.read_csv(csv_path)

        self.df["Order_Date"] = pd.to_datetime(
            self.df["Order_Date"]
        )


    def total_sales(self):
        return float(
            self.df["Amount"].sum()
        )


    def total_orders(self):
        return int(
            len(self.df)
        )


    def cancelled_orders(self):
        return int(
            (self.df["Status"] == "Cancelled").sum()
        )


    def returned_orders(self):
        return int(
            (self.df["Status"] == "Returned").sum()
        )


    def sales_by_category(self):
        return (
            self.df
            .groupby("Category")["Amount"]
            .sum()
            .to_dict()
        )


    def sales_by_region(self):
        return (
            self.df
            .groupby("Region")["Amount"]
            .sum()
            .to_dict()
        )


    def summary(self):

        return {
            "total_sales": self.total_sales(),
            "total_orders": self.total_orders(),
            "cancelled_orders": self.cancelled_orders(),
            "returned_orders": self.returned_orders(),
            "sales_by_category": self.sales_by_category(),
            "sales_by_region": self.sales_by_region()
        }