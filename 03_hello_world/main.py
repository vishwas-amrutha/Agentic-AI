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

response = client.chat.completions.create(
    model="openai/gpt-oss-20b", # Using a supported Groq model
    messages=[
        {"role": "system", "content": "You are an expert in mathematics , only answer maths questions, if not maths just say sorry, i can only answer fucking maths questions"}, # setting up context for the model
        {"role": "user", "content": "hey tell me a joke"} # user query
    ]
)

print(response.choices[0].message.content)

"""
we are using openai sdk with grok api key
"""