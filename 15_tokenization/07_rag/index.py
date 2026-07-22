from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

dotenv_path = Path(__file__).resolve().parent.parent/".env"
pdf_path = Path(__file__).parent/"React-Ebook-Filestack.pdf"

load_dotenv(dotenv_path=dotenv_path)

loader = PyPDFLoader(file_path=pdf_path)

docs  = loader.load()



# split docs in smaller chunk
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 400
)

chunks = text_splitter.split_documents(documents=docs)

# vector embeddings for this chunk 


embedding_model = OpenAIEmbeddings(
    model='text-embedding-3-large'
)

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url='http://localhost:6333',
    collection_name = 'learning_react'
)

print("Indexing of documents done ....")