from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / '.env'
print(env_path)

load_dotenv(dotenv_path=env_path)

client = OpenAI()

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {
            'role':"system",
            'content':"YOu are an expert in maths and only answer maths related questions"
        },
        {
            'role':"user",
            'content':'Hey can you help me solve a + b whole square'
        }
    ]
)


print(response.choices[0].message.content)