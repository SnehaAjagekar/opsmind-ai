import streamlit as st
from src.router import OpsMindRouter


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="OpsMind AI",
    page_icon="🤖",
    layout="wide"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🤖 OpsMind AI")
st.write("AI Business Document & Data Assistant")

st.divider()


# --------------------------------------------------
# LOAD OPSMIND ROUTER
# --------------------------------------------------

@st.cache_resource
def load_opsmind():
    document_path = "src/data/documents/company_policy.txt"
    csv_path = "src/data/csv/orders.csv"

    return OpsMindRouter(
        document_path,
        csv_path
    )


router = load_opsmind()


# --------------------------------------------------
# QUESTION INPUT
# --------------------------------------------------

st.subheader("💬 Ask OpsMind AI")

question = st.text_input(
    "Enter your business question:",
    placeholder="Example: What is the refund policy?"
)


# --------------------------------------------------
# ASK BUTTON
# --------------------------------------------------

if st.button("Ask AI", type="primary"):

    if not question.strip():
        st.warning("Please enter a question.")

    else:

        with st.spinner("Thinking..."):

            result = router.ask(question)


        # --------------------------------------------------
        # SHOW ROUTE
        # --------------------------------------------------

        if result["route"] == "rag":

            st.info("🔎 Question answered using company documents.")

        else:

            st.info("📊 Question answered using business data.")


        # --------------------------------------------------
        # SHOW ANSWER
        # --------------------------------------------------

        st.subheader("🤖 AI Answer")

        st.write(result["answer"])


        # --------------------------------------------------
        # SHOW SOURCES FOR RAG
        # --------------------------------------------------

        if result["route"] == "rag" and result["sources"]:

            st.subheader("📄 Retrieved Information")

            for i, source in enumerate(result["sources"], start=1):

                with st.expander(f"Source {i}"):

                    st.write(source["text"])

                    st.caption(
                        f"Similarity distance: "
                        f"{source['distance']:.4f}"
                    )


# --------------------------------------------------
# BUSINESS DATA DASHBOARD
# --------------------------------------------------

st.divider()

st.subheader("📊 Business Data Overview")


summary = router.business_ai.analyzer.summary()


col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Total Sales",
    f"₹{summary['total_sales']:,.0f}"
)

col2.metric(
    "Total Orders",
    summary["total_orders"]
)

col3.metric(
    "Cancelled Orders",
    summary["cancelled_orders"]
)

col4.metric(
    "Returned Orders",
    summary["returned_orders"]
)


# --------------------------------------------------
# SALES BY CATEGORY
# --------------------------------------------------

st.subheader("Sales by Category")

st.bar_chart(
    summary["sales_by_category"]
)


# --------------------------------------------------
# SALES BY REGION
# --------------------------------------------------

st.subheader("Sales by Region")

st.bar_chart(
    summary["sales_by_region"]
)