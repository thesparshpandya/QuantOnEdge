import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

DB_PATH = os.path.join("data", "vector_db")

def get_qa_chain():
    # 1. Load the DB
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory=DB_PATH, embedding_function=embedding_function)
    
    # 2. Connect to Ollama (Llama 3)
    llm = Ollama(model="llama3") 
    
    # 3. Create the Chain
    retriever = db.as_retriever(search_kwargs={"k": 3})
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    
    return qa_chain

if __name__ == "__main__":
    chain = get_qa_chain()
    # You can change this question
    query = "What are the key risks mentioned in the report?"
    print(f"Thinking about: {query}...")
    response = chain.invoke(query)
    print("\nAnswer:\n", response['result'])