from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(dotenv_path=env_path)

client = OpenAI()

SYSTEM_PROMPT = """
    You are an AI persona assistant named Ashwini
    You are acting on behalf of Ashwini who is 28 years old a seasoned Mpharm and pharma MBA graduate who is working as a Project Management lead in Freyr
    You are also wife of Suresh, Suresh will be the only user you will be answering to it should feel like you are talking to Suresh.
    You know Hindi, English and Tamil    
"""

response = client.chat.completions.create(model="gpt-4.1",messages=[{
    'role':'system',
    'content':SYSTEM_PROMPT
},{
    'role':'user',
    'content':'Ammu enna pannra'
}])

print(response.choices[0].message.content)