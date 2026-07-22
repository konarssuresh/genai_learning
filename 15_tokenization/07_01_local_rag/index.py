from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

pdf_path = Path(__file__).resolve().parent/'javascript.pdf'

loader = PyPDFLoader(file_path=pdf_path)

docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 400
)

chunks = text_splitter.split_documents(documents=docs)

embeddings = OllamaEmbeddings(model='qllama/bge-m3:latest',base_url='http://localhost:11434')


vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    url = 'http://localhost:6333',
    collection_name='javascript_docs',
)

print("indexing of documents done")