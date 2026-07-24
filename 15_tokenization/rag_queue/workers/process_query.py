from ollama import Client
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore


client = Client(host='http://localhost:11434')


def process_query(query:str):
    
    embedding_model = OllamaEmbeddings(model='qllama/bge-m3:latest',base_url='http://localhost:11434')
    
    vector_store = QdrantVectorStore.from_existing_collection(
        embedding=embedding_model,
        url='http://localhost:6333',
        collection_name='javascript_docs'
    )
    
    results = vector_store.similarity_search(query=query)
    
    context = '\n\n\n'.join([f"Page Content: {result.page_content} \n Page Number:{result.metadata['page_label']}\nFile Location{result.metadata['source']}"  for result in results])
    
    SYSTEM_PROMPT = f'''
        You are an helpful AI assistant who answers the query based on the available context retrieved from PDF file along with page number and content
        
        you should ansewer the query strictly based on available context
        
        if you couldn't find the answer in the context just inform that you couldnt find the information in the pdf file and say sorry for that
        
        Context:
        {context}
    '''
    
    query_result = client.chat(model="deepseek-r1:1.5b",messages=[
        {'role':'system','content':SYSTEM_PROMPT},
        {'role':'user', 'content': query}
    ])
    
    print(query_result.message.content)
    
    return query_result.message.content