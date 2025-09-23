import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

repo_path = r"C:\Users\franc\Desktop\ProjLEI\ProjetoLEI"

# Carregar só arquivos Java
loader = DirectoryLoader(
    repo_path,
    glob="**/*.java"
)
docs = loader.load()
docs = [doc for doc in docs if doc.page_content.strip() != ""]
print(f"Total de documentos carregados: {len(docs)}")

# Dividir em chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
split_docs = text_splitter.split_documents(docs)
split_docs = [doc for doc in split_docs if doc.page_content.strip() != ""]
print(f"Total de chunks válidos: {len(split_docs)}")

# Embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Criar ou abrir base Chroma (persistência automática)
vectordb = Chroma.from_documents(
    split_docs,
    embeddings,
    collection_name="lemmings",
    persist_directory="./chroma_db"
)
print("ChromaDB local criado ou atualizado em ./chroma_db")

# Testar query
query = "FornecedorBomba"
docs_found = vectordb.similarity_search(query, k=5)
print(f"Resultados para '{query}': {len(docs_found)}")
for doc in docs_found:
    print(doc.page_content[:300])
