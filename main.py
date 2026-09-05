from loader import load_paper
from rag_engine import build_vectorstore, build_qa_chain
from agent import ResearchAssistant

def main():
    pdf_path = input("Enter path to the research paper PDF: ").strip()
    print("Loading paper...")
    pages, full_text = load_paper(pdf_path)

    print("Indexing paper for retrieval...")
    vectorstore = build_vectorstore(pages)
    qa_chain = build_qa_chain(vectorstore)
    assistant = ResearchAssistant(full_text, qa_chain)

    print("\nReady! Try: 'summary', 'contributions', 'limitations', 'future work',")
    print("or ask any question about the paper. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            break
        response = assistant.route(user_input)
        print(f"\nAssistant: {response}\n")

if __name__ == "__main__":
    main()