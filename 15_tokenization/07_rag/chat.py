from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

dotenv_path = Path(__file__).resolve().parent.parent/".env"

load_dotenv(dotenv_path=dotenv_path)

openai_client = OpenAI()

embedding_model = OpenAIEmbeddings(
    model='text-embedding-3-large'
)

vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url='http://localhost:6333',
    collection_name = 'learning_react'
)

# take the user input 

user_query = input("Ask something about react")

# relevant chunks from the vector db
search_results = vector_store.similarity_search(query=user_query)

context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number:{result.metadata['page_label']}\nFile Location{result.metadata['source']}" for result in search_results])

SYSTEM_PROMPT = f'''
    you are a helpful AI assistant named React Guru who answers relevant questions related to React based on the available context retrieved from a PDF file along with page_contents and page number. 
    you should only answer to user based on the following context and navigate the user to open right page number to know more
    
    Context:
    {context}
'''

response = openai_client.chat.completions.create(model='gpt-4',messages=[
    {'role':'system','content': SYSTEM_PROMPT},
    {'role':'user','content':user_query}
])

print(response.choices[0].message.content)