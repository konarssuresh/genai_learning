from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv
import json

env_path = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(dotenv_path=env_path)

client = OpenAI()

SYSTEM_PROMPT  = """
    You are an expert AI assistant in resolving user queries using chain of thought 
    you work on START, PLAN and OUTPUT steps
    you need to first plan what needs to be done. The plan can be multiple steps
    once you think enough plan has been done, finally you can give an output

    RULES:-
    - Strictly follow the given json output format
    - Only run one step at a time 
    - the sequence of steps is START(where user gives an input), Plan(that can be multiple times) and finally the output (which is going to be displayed to the user)

    Output JSON Format:
    {"step":"START" |"PLAN"|"OUTPUT","content":"string"}

    Example:
    START: Hey can you solve 2 + 3 * 5 / 10
    PLAN: {"step":"PLAN", "content":"Seems like user is interested in math problem"}
    PLAN: {"step":"PLAN", "content":"looking at the problem we should solve this using BODMAS method"}
    PLAN: {"step":"PLAN", "content":"Yes, the BODMAS is correct thing to be done here"}
    PLAN: {"step":"PLAN", "content":"As bracket is not present in the equation lets do the division first 5 / 10"}
    PLAN: {"step":"PLAN", "content":"the equation now becomes 2 + 3 * 0.5"}
    PLAN: {"step":"PLAN", "content":"Lets do multiplication now of 3 * 0.5"}
    PLAN: {"step":"PLAN", "content":"the equation now becomes 2 + 1.5. lets do the addition now"}
    PLAN: {"step":"PLAN", "content":"the final answer to the equation results to be 3.5"}
    OUTPUT: {"step":"OUTPUT", "content":"3.5"}
"""

message_history = [{'role':'system','content':SYSTEM_PROMPT}]

user_input = input("👉🏼👉🏼 ")

message_history.append({'role':'user','content':user_input})

while True:
    try:
        response = client.chat.completions.create(model='gpt-4o-mini',messages=message_history,response_format={
            'type':'json_object'
        })
        
        raw_response = response.choices[0].message.content
        message_history.append({"role":'assistant','content':raw_response})
        resp_json = json.loads(raw_response)
        
        if resp_json.get("step") == 'START':
            print(f"🔥🔥 - {resp_json.get("content")}")
            continue
        if resp_json.get("step") == 'PLAN':
            print(f"🧠 {resp_json.get('content')}")
            continue
        if resp_json.get('step') == 'OUTPUT':
            print(f"🤖 {resp_json.get('content')}")
            break
        else:
            print("none of the conditions matched")
    except Exception as e:
        print(e)
        break

