import os
from openai import OpenAI
from dotenv import load_dotenv
import json


load_dotenv()


client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
)


SYSTEM_PROMPT = """ 
    You are expert AI assistant, expert in user queries using chain of though,
    you work on START, PLAN and OUTPUT steps
    You need to first plan qhat needs to be done and then execute it
    
    Rules:
    - Strictly follow the output format as json
    - only run one step at a time
    - the sequence of steps should be START(where the user gives an input), PLAN(can be multiple times) and OUTPUT(which is going to be display to the user)
    
    Format JSON format:
    {
        "step": "START" | "PLAN" | "OUTPUT",
        "content": "string"
    }

    Example:
    - START: "Can you solve 2+3*5/10"
    - PLAN: {"step": "Plan", "content": "seems like user is intrested in math problem"}
    - PLAN: {"step": "Plan", "content": "looking at the problem it should be solved using bodmas rule"}
    - PLAN: {"step": "Plan", "content": "first i should solve the division part"}
    - PLAN: {"step": "Plan", "content": "then i should solve the multiplication part"}
    - PLAN: {"step": "Plan", "content": "then i should solve the addition part"}
    - PLAN: {"step": "Plan", "content": "finally i should give the answer to the user"}
    - OUTPUT: {"step": "Output", "content": "the answer is 8.5"}

"""

USER_PROMPT = "Write a code to add n numbers"

response = client.chat.completions.create(
    model="openai/gpt-oss-20b", 
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT}, 
        {"role": "user", "content": USER_PROMPT},
        # manually appending the outputs we get from above inputs
        {"role": "assistant", "content": json.dumps({"step":"START","content":"you wat to add n numbers"})},
        {"role": "assistant", "content": json.dumps({"step":"PLAN","content":"Plan: \n1. Choose a programming language (Python). \n2. Prompt the user for the number of values n. \n3. Initialize a sum variable to 0. \n4. Use a loop to read n numbers from the user, converting each to float/int. \n5. Add each number to the sum. \n6. After the loop, print or return the total sum."})},
        {"role": "assistant", "content": json.dumps({"step": "OUTPUT", "content": "Here is a simple Python script that adds *n* numbers together:\n\n```python\n# Add n numbers – Python example\n\ndef add_n_numbers():\n    try:\n        # Ask the user how many numbers will be entered\n        n = int(input(\"How many numbers do you want to add? \"))\n        if n <= 0:\n            print(\"Please enter a positive integer.\")\n            return\n    except ValueError:\n        print(\"That isn’t a valid integer. Exiting.\")\n        return\n\n    total = 0.0  # use float to handle decimal inputs\n\n    for i in range(1, n + 1):\n        while True:\n            try:\n                val = float(input(f\"Enter number {i}: \"))\n                break\n            except ValueError:\n                print(\"Invalid number, please try again.\")\n        total += val\n\n    print(f\"The total sum of the {n} numbers is: {total}\")\n\nif __name__ == \"__main__\":\n    add_n_numbers()\n```\n\n### How it works\n1. **Prompt for `n`** – The script asks how many numbers the user wants to add.\n2. **Input loop** – For each of the `n` numbers, it repeatedly prompts until a valid numeric value is entered.\n3. **Summation** – It accumulates the numbers in the `total` variable.\n4. **Result** – After all inputs are collected, the script prints the final sum.\n\nYou can copy and run this script in any Python environment (Python 3.x). Feel free to adapt it to another language if needed!"})},
        

    ]
)

print(response.choices[0].message.content)

"""
the reason we have added is to make the model know the history of the conversation

"""