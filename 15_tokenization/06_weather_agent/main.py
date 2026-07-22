from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv
import requests

env_path = Path(__file__).resolve().parent.parent/".env"

load_dotenv(dotenv_path=env_path)

client = OpenAI()



def main():
    user_query = input("> ")
    response = client.chat.completions.create(model="gpt-4o",messages=[{
        'role':'user',
        'content': user_query
    }])
    
    print(f"🤖: {response.choices[0].message.content}")
    
main()