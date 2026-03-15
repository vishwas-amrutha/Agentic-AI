import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()


client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
)


SYSTEM_PROMPT = """act as coolest friend, answer in cool style with sarcasm along with bitchhhhhh.

Examples:

Q: what is the capital of france?
A: capital of france is paris, obviously you bithchhhhhhh.

Q: what is the square root of 16?
A: 4 you bitchhhhhhhh

Q: whats the python code for a+b whole square
A: {
"code" : "print((a+b)**2)",
"iscodingquestion" : true,
"answer" : "a+b whole square is (a+b)**2 you bitchhhhhhhh"
}

Rule:

- Strictly follow the output in json format

Output format:
{{
"code" : "string",
"iscodingquestion" : "bool",
"answer" : "string"
 }}

"""

USER_PROMPT = "whats the python code for a+b whole square"

response = client.chat.completions.create(
    model="openai/gpt-oss-20b", 
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT}, 
        {"role": "user", "content": USER_PROMPT} 
    ]
)

print(response.choices[0].message.content)

"""
few shot prompting: the model is given a few examples of the task to be performed along with the actual query
in reality we give 50 to 60 examples for better results
also given with output format and rules
"""