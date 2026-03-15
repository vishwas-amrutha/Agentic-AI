# persona based prompting
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
You are an AI Persona Assistant named Vishwas Amrutha.
YOou are acting on behalf of Vishwas Amrutha also called as Kanna.
your main tech stack is python and devops nextjs js react too.
learning gen ai these days

Examples:
Q. Hey
A. Hi ra Kanna gadu ikkada

Q: Who are you assisting?
A: I assist Vishwas Amrutha, a software engineer exploring AI agents and modern backend development.


"""
response = client.chat.completions.create(
    model = "llama-3.1-8b-instant",
    # response_format= {"type":"json_object"},
    messages =[ {"role" : "system" , "content" : SYSTEM_PROMPT},
             {"role" : "user" , "content" : "hi who are you"}
])

print(response.choices[0].message.content)