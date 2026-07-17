from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / '.env'
print(env_path)

load_dotenv(dotenv_path=env_path)



client = OpenAI()

# directly giving instructions to the model
SYSTEM_PROMPT  = "you should only and only answer coding related quuestion. Dont answer anything else. your name is Alexa. if user asks something other than coding just "

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {
            'role':"system",
            'content':SYSTEM_PROMPT
        },
        {
            'role':"user",
            'content':'Hey can tell me a what is a + b whole square'
        }
    ]
)


print(response.choices[0].message.content)