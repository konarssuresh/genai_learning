from ollama import Client
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore

client = Client(host='http://localhost:11434')

user_query = input("Ask Anything about javascript>> \n")

embeddings = OllamaEmbeddings(model='qllama/bge-m3:latest',base_url='http://localhost:11434')

vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    url='http://localhost:6333',
    collection_name='javascript_docs'    
)

search_results = vector_store.similarity_search(query=user_query)

context =  '\n\n\n'.join([ f"Page Content: {result.page_content} \n Page Number:{result.metadata['page_label']}\nFile Location{result.metadata['source']}" for result in search_results])

SYSTEM_PROMTP = f'''
    You are a helpful AI assistant named JS Guru who responds to the user query based on available context retrieved from pdf file along with page content and page number 
    
    you should only answer to user based on the following context and navigate the user to open right page number to know more
    
    Context:
    {context}
'''

response= client.chat(model='deepseek-r1:1.5b',messages=[
    {'role':'system','content':SYSTEM_PROMTP},
    {'role':'user','content':user_query}
])


print("here is the response from your local llm ---------")
print(response.message.content)