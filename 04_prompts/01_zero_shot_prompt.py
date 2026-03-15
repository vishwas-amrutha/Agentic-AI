import os
from openai import OpenAI
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# The client will automatically look for the OPENAI_API_KEY environment variable.
# We point the base_url to Groq's API instead of OpenAI's.
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
)

# zero shot prompt: the model is given a direct question or task without prior examples
SYSTEM_PROMPT = "act as strict maths teacher, tell sorry directly if question is not related to maths."

USER_PROMPT = "hey can you translate this sentence to french: 'i love you'"

response = client.chat.completions.create(
    model="openai/gpt-oss-20b", # Using a supported Groq model
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT}, # setting up context for the model
        {"role": "user", "content": USER_PROMPT} # user query
    ]
)

print(response.choices[0].message.content)

"""
zero shot prompt: the model is given a direct question or task without prior examples
"""