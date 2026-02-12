import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

# Define paths relative to where we run the script
PDF_FOLDER = os.path.join("data", "pdfs")
DB_PATH = os.path.join("data", "vector_db")

def ingest_documents():
    # 1. Load PDFs
    documents = []
    print(f"Scanning for PDFs in: {PDF_FOLDER}")
    
    if not os.path.exists(PDF_FOLDER):
        os.makedirs(PDF_FOLDER)
        print(f"Created folder {PDF_FOLDER}. Please drop a PDF there!")
        return

    for file in os.listdir(PDF_FOLDER):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(PDF_FOLDER, file)
            print(f"Loading: {file}...")
            loader = PyPDFLoader(pdf_path)
            documents.extend(loader.load())
    
    if not documents:
        print("No PDFs found!")
        return

    # 2. Split Text
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(documents)
    
    # 3. Save to Vector DB
    print("Creating Vector DB... This might take a minute.")
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_documents(chunks, embedding_function, persist_directory=DB_PATH)
    print(f"Success! Saved {len(chunks)} chunks to {DB_PATH}")

if __name__ == "__main__":
    ingest_documents()