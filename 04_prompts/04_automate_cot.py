import os
from openai import OpenAI
from dotenv import load_dotenv
import json


load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)


SYSTEM_PROMPT = """ 
    You are expert AI assistant, expert in user queries using chain of though,
    you work on START, PLAN and OUTPUT STEPs
    You need to first plan qhat needs to be done and then execute it
    
    Rules:
    - Strictly follow the output format as json
    - only run one STEP at a time
    - the sequence of STEPs should be START(where the user gives an input), PLAN(can be multiple times) and OUTPUT(which is going to be display to the user)
    
    Format JSON format:
    {
        "STEP": "START" | "PLAN" | "OUTPUT",
        "content": "string"
    }

    Example:
    - START: "Can you solve 2+3*5/10"
    - PLAN: {"STEP": "Plan", "content": "seems like user is intrested in math problem"}
    - PLAN: {"STEP": "Plan", "content": "looking at the problem it should be solved using bodmas rule"}
    - PLAN: {"STEP": "Plan", "content": "first i should solve the division part"}
    - PLAN: {"STEP": "Plan", "content": "then i should solve the multiplication part"}
    - PLAN: {"STEP": "Plan", "content": "then i should solve the addition part"}
    - PLAN: {"STEP": "Plan", "content": "finally i should give the answer to the user"}
    - OUTPUT: {"STEP": "Output", "content": "the answer is 8.5"}

"""
print("\n\n\n")

message_history = [
    {"role":"system", "content" : SYSTEM_PROMPT}
]

user_query = input("user input : ")
message_history.append({"role": "user", "content" : user_query})

while True:
    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        response_format= {"type":"json_object"},
        messages = message_history
    )

    raw_result = response.choices[0].message.content
    message_history.append({"role" : "assistant", "content": raw_result})
    parsed_result = json.loads(raw_result)

    if parsed_result["STEP"] == "START":
        print("Starting LLM loop: ",parsed_result.get("content"))
    if parsed_result["STEP"] == "PLAN":
        print("Thinking.....,",parsed_result.get("content"))
    if parsed_result["STEP"] == "OUTPUT":
        print("FInal output is :",parsed_result["content"])
        break

print("\n\n\n")

"""
This code creates a simple AI reasoning agent that uses an LLM through the Groq OpenAI API.
It takes a user query, sends it to the model with a system prompt that enforces a structured reasoning format 
(START → PLAN → OUTPUT), and repeatedly calls the model in a loop. The model returns JSON responses,
which the program parses and prints step-by-step thinking (PLAN) until it reaches the final answer (OUTPUT),
where the loop stops.

"""