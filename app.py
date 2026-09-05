import streamlit as st
from loader import load_paper
from rag_engine import build_vectorstore, build_qa_chain
from agent import ResearchAssistant

st.title("📄 Research Paper Assistant")

uploaded_file = st.file_uploader("Upload a research paper (PDF)", type="pdf")

if uploaded_file:
    with open("temp_paper.pdf", "wb") as f:
        f.write(uploaded_file.read())

    if "assistant" not in st.session_state:
        with st.spinner("Reading and indexing the paper..."):
            pages, full_text = load_paper("temp_paper.pdf")
            vectorstore = build_vectorstore(pages)
            qa_chain = build_qa_chain(vectorstore)
            st.session_state.assistant = ResearchAssistant(full_text, qa_chain)
        st.success("Paper indexed! Ask away.")

    assistant = st.session_state.assistant

    col1, col2, col3, col4 = st.columns(4)
    if col1.button("Summary"):
        st.write(assistant.summarize())
    if col2.button("Contributions"):
        st.write(assistant.contributions())
    if col3.button("Limitations"):
        st.write(assistant.limitations())
    if col4.button("Future Work"):
        st.write(assistant.future_work())

    question = st.text_input("Ask a question about the paper:")
    if question:
        answer, pages_cited = assistant.ask(question)
        st.write(answer)
        st.caption(f"Source pages: {pages_cited}")