from fastapi import FastAPI,Query
from .client.queue import query_queue
from .workers.process_query import process_query


app = FastAPI()

@app.get("/")
def base_health_check():
    return {
        "status":"running",
        "service_name":"Local_Rag_Server"
    }
    
@app.post("/chat")
def process_chat(user_query=Query(...,description='the query that user has')):
    
    job = query_queue.enqueue(process_query,user_query)
    
    return {"status":"queued","job_id":job.id}

@app.get("/job-status")
def get_result(job_id=Query(...,description='The id of the job which was rreturned from /chat api')):
    job = query_queue.fetch_job(job_id=job_id)
    result = job.return_value()
    return {"result": result}