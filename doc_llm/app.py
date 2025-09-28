from fastapi import FastAPI
from pydantic import BaseModel

# LangChain imports
from langchain_community.llms import GPT4All
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA

app = FastAPI()

# Embeddings locais
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Vetor store Chroma
vectordb = Chroma(
    persist_directory="./chroma_db",
    collection_name="lemmings",
    embedding_function=embeddings
)
retriever = vectordb.as_retriever()

# Caminho para o modelo offline
model_path = r"C:\Users\franc\AppData\Local\nomic.ai\GPT4All\qwen2.5-coder-7b-instruct-q4_0.gguf"

# LLM local offline
llm = GPT4All(
    model=model_path,
    n_threads=4,
    backend="gptj"
)

# Cria a cadeia de QA
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff"
)

# Modelo para receber queries
class Query(BaseModel):
    pergunta: str

import json

@app.post("/perguntar")
def perguntar(query: Query):
    resposta = qa.invoke(query.pergunta)
    texto = resposta["result"]

    # json mantendo acentos e caracteres especiais
    return json.loads(json.dumps({"resposta": texto}, ensure_ascii=False))

