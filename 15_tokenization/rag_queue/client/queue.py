from redis import Redis
from rq import Queue


query_queue = Queue(connection=Redis(host='localhost',port='6379'))



