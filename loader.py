from langchain_community.document_loaders import PyPDFLoader

def load_paper(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()  # one LangChain Document per PDF page
    full_text = "\n".join(p.page_content for p in pages)
    return pages, full_text

if __name__ == "__main__":
    pages, text = load_paper("sample_paper.pdf")
    print(f"Loaded {len(pages)} pages")
    print(text[:500])