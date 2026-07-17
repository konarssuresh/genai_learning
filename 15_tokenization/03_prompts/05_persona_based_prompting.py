from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(dotenv_path=env_path)

client = OpenAI()

SYSTEM_PROMPT = """

"""

response = client.chat.completions.create(model="gpt-4o-mini",messages=[{
    'role':'system',
    'content':SYSTEM_PROMPT
},{
    'role':'user',
    'content':''
}])

print(response.choices[0].message.content)