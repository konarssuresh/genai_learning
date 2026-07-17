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

    Rule:
    - Strictly follow the output in json format

    output format:
    {{
        "code":"string" or None,
        "isCodingQuestion": boolean
    }}

    Examples:
    q: can you explain a + b whole square?
    A:  {{
        "code":None,
        "isCodingQuestion": false
    }}

    Q: Hey , write a code in python to add two numbers
    A:     {{
        "code":"def add(a,b):
            return a + b
        ",
        isCodingQuestion": boolean
    }}
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
            'content':'give me program to add n numbers in js'
        }
    ]
)


print(response.choices[0].message.content)


# few shot prompting 