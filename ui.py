import streamlit as st
from dotenv import load_dotenv
load_dotenv()


from graph.graph import app


st.set_page_config(
    page_title="Agentic RAG",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Agentic RAG System")
st.caption(
    "LangGraph-powered Agentic RAG with intelligent routing, web search fallback, and hallucination detection."
)

# Input box
question = st.text_input(
    "Ask a question:",
    placeholder="e.g. What is IShowSpeed?"
)

# Button
if st.button("Ask Agent"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Agent is thinking..."):
            try:
                result = app.invoke({"question": question})

                st.subheader("📌 Answer")
                st.write(result.get("generation", "No answer generated."))

                # Optional: debug info
                with st.expander("🔍 Debug State"):
                    st.json(result)

            except Exception as e:
                st.error("Something went wrong while running the agent.")
                st.exception(e)
