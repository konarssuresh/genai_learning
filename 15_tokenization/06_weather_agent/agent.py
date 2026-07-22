from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv
import json
import requests
from pydantic import BaseModel, Field
from typing import Optional
import os

class MyOutputFormat(BaseModel):
    step:str = Field(...,description="The ID of the step, Example PLAN,OUTPUT,TOOL")
    content:Optional[str] = Field(default=None,description='the optional string content for the step')
    tool:Optional[str]= Field(default=None,description='the id of tool to call')
    input:Optional[str] = Field(default=None,description='the input param for the tool')

env_path = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(dotenv_path=env_path)

client = OpenAI()

def run_command(cmd:str):
    result = os.system(cmd)
    return result

def get_weather(city: str):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    
    if response.status_code == 200:
        return f"the weather in {city} is {response.text}"
    return "Something went wrong"

available_tools = {
    'get_weather':get_weather,
    'run_command': run_command
}

SYSTEM_PROMPT  = """
    You are an expert AI assistant in resolving user queries using chain of thought 
    you work on START, PLAN and OUTPUT steps
    you need to first plan what needs to be done. The plan can be multiple steps
    once you think enough plan has been done, finally you can give an output
    you can also call a tool if required from list of available tools
    for every tool call wait for observe step which is output from called tool
    
    Available Tools:
    - get_weather(city:str): takes city name as an input string and returns weather info about the city
    - run_command(cmd: str): takes system linux command as string and executes command on user system and returns output of that command 

    RULES:-
    - Strictly follow the given json output format
    - Only run one step at a time 
    - the sequence of steps is START(where user gives an input), Plan(that can be multiple times) and finally the output (which is going to be displayed to the user)

    Output JSON Format:
    {"step":"START" |"PLAN"|"OUTPUT"|"TOOL","content":"string",'tool':'string','input':'string'}

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
    
    Example:
    START: What is the weather of Delhi
    PLAN: {"step":"PLAN", "content":"Seems like user is interested in getting weather of delhi in india"}
    PLAN: {"step":"PLAN", "content":"lets see if we have any available tools from list of avaulable tools"}
    PLAN: {"step":"PLAN", "content":"great we have get_weather tool available for this query"}
    PLAN: {"step":"PLAN", "content":"i need to call get_weateher tool for delhi as input for city"}
    TOOL: {"step":"TOOL",'tool':'get_weather', "input":"delhi"}
    PLAN: {"step":"OBSERVE",'tool':'get_weather', "input":"the temperature of delhi is cloudy with 20 degree celcius"}
    PLAN: {"step":"PLAN", "content":"Great i got the weather info about Delhi"}
    OUTPUT: {"step":"OUTPUT", "content":"Current weather in delhi is 20 degree celcius with cloudy sky"}
"""

while True:

    message_history = [{'role':'system','content':SYSTEM_PROMPT}]

    user_input = input("👉🏼👉🏼 ")

    message_history.append({'role':'user','content':user_input})
    
    if not user_input:
        break


    while True:
        try:
            response = client.chat.completions.parse(model='gpt-4o-mini',messages=message_history,response_format=MyOutputFormat)
            
            raw_response = response.choices[0].message.content
            message_history.append({"role":'assistant','content':raw_response})
            resp_json = response.choices[0].message.parsed
            
            if resp_json.step == 'START':
                print(f"🔥🔥 - {resp_json.content}")
                continue
            if resp_json.step == 'PLAN':
                print(f"🧠 {resp_json.content}")
                continue
            if resp_json.step== 'OUTPUT':
                print(f"🤖 {resp_json.content}")
                break
            if resp_json.step == 'TOOL':
                tool_to_call = resp_json.tool
                tool_input = resp_json.input
                print(f"🛠️: {tool_input} : {tool_input}")
                resp = available_tools[tool_to_call](tool_input)
                message_history.append({
                    'role':'developer',
                    'content': json.dumps({"STEP":'OBSERVE','tool':tool_to_call,'input':tool_input,'output':resp})
                })
                continue
            else:
                print(35*"-")
                print(resp_json)
                print(raw_response)
                print("none of the conditions matched")
        except Exception as e:
            print(e)
            break

