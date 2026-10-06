from src.rag_pipeline import RAGPipeline
from src.business_ai import BusinessAI


class OpsMindRouter:

    def __init__(self, document_path, csv_path):

        print("Initializing OpsMind AI...")

        self.rag = RAGPipeline(document_path)

        self.business_ai = BusinessAI(csv_path)

        print("OpsMind AI initialized successfully.")


    def route_question(self, question: str):

        """
        Decide whether the question should be answered
        using business data or company documents.
        """

        question_lower = question.lower()

        # Business data keywords
        data_keywords = [
            "sales",
            "revenue",
            "orders",
            "order count",
            "number of orders",
            "region",
            "category",
            "cancelled",
            "cancelled orders",
            "returned orders",
            "amount",
            "highest sales",
            "lowest sales",
            "total sales",
            "total orders",
            "sales by region",
            "sales by category"
        ]

        for keyword in data_keywords:

            if keyword in question_lower:
                return "business"

        return "rag"


    def ask(self, question: str):

        """
        Route the question to the correct tool.
        """

        route = self.route_question(question)


        # Business question
        if route == "business":

            answer = self.business_ai.ask(question)

            return {
                "route": "business",
                "answer": answer,
                "sources": []
            }


        # Document / RAG question
        else:

            result = self.rag.ask(question)

            return {
                "route": "rag",
                "answer": result["answer"],
                "sources": result["sources"]
            }














# from src.rag_pipeline import RAGPipeline
# from src.business_ai import BusinessAI


# class OpsMindRouter:

#     def __init__(self, document_path, csv_path):

#         print("Initializing OpsMind AI...")

#         self.rag = RAGPipeline(
#             document_path
#         )

#         self.business_ai = BusinessAI(
#             csv_path
#         )

#         print("OpsMind AI initialized successfully.")


# def route_question(self, question: str):
#     """
#     Decide whether the question should be answered
#     using business data or company documents.
#     """

#     question_lower = question.lower()


#     # --------------------------------------------------
#     # Business data keywords
#     # --------------------------------------------------

#     data_keywords = [
#         "sales",
#         "revenue",
#         "orders",
#         "order count",
#         "number of orders",
#         "region",
#         "category",
#         "cancelled",
#         "cancelled orders",
#         "returned orders",
#         "amount",
#         "highest sales",
#         "lowest sales",
#         "total sales",
#         "total orders",
#         "sales by region",
#         "sales by category"
#     ]


#     # --------------------------------------------------
#     # Check business-data questions
#     # --------------------------------------------------

#     for keyword in data_keywords:

#         if keyword in question_lower:

#             return "business"


#     # --------------------------------------------------
#     # Everything else goes to RAG
#     # --------------------------------------------------

#     return "rag"

#     def ask(self, question: str):

#         route = self.route_question(
#             question
#         )

#         if route == "business":

#             answer = self.business_ai.ask(
#                 question
#             )

#             return {
#                 "route": "business",
#                 "answer": answer,
#                 "sources": []
#             }

#         else:

#             result = self.rag.ask(
#                 question
#             )

#             return {
#                 "route": "rag",
#                 "answer": result["answer"],
#                 "sources": result["sources"]
#             }