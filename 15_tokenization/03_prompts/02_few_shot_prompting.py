from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / '.env'
print(env_path)

load_dotenv(dotenv_path=env_path)



client = OpenAI()

# few show prompting - direct instructions with few examples to model
SYSTEM_PROMPT  = """
    You should only answer the coding related questions. Donot answer anything else 
    your name is Alexa. is user asks anything else other than coding , just say sorry.

    Examples:
    q: can you explain a + b whole square?
    A: sorry, i can only help with coding related question

    Q: Hey , write a code in python to add two numbers
    A: def add(a,b):
            return a + b
"""

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {
            'role':"system",
            'content':SYSTEM_PROMPT
        },
        {
            'role':"user",
            'content':'Hey can tell me a what is a + b whole cube'
        }
    ]
)


print(response.choices[0].message.content)


# few shot prompting 