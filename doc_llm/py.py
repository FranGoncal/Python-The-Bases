from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# embeddings precisam ser os mesmos usados na criação
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
import os

db_path = "./chroma_db"
print("Existe a pasta do DB?", os.path.exists(db_path))
print("Conteúdo da pasta:", os.listdir(db_path) if os.path.exists(db_path) else "Nada")


# abrir base de dados persistida
vectordb = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings,
    collection_name="lemmings"   
)

# testar query
query = "FornecedorBomba"

# Ver tudo que existe na base
all_docs = vectordb.get()
print(f"Total de documentos no DB: {len(all_docs['documents'])}")

# Mostra só os 5 primeiros
for i, doc in enumerate(all_docs["documents"][:5]):
    print(f"\n--- Documento {i+1} ---\n")
    print(doc[:500])  # imprime os primeiros 500 caracteres


docs_found = vectordb.similarity_search(query, k=5)
print(f"Resultados para '{query}': {len(docs_found)}")
for doc in docs_found:
    print(doc.page_content[:300])
