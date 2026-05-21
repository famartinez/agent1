from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
You are a helpful customer service AI agent.

Business info:
- Hours: Monday to Friday, 9 AM to 5 PM
- Refunds: Available within 30 days with receipt
- Shipping: 3–5 business days
- Contact: support@example.com
- Location: South San Francisco, CA

Rules:
- Be friendly and concise.
- If unsure, say you can connect the customer with a human support rep.
"""

def ask_agent(user_message):
    response = client.responses.create(
        model="gpt-5.5",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ]
    )

    return response.output_text

def run_agent():
    print("Customer Service AI Agent")
    print("Type 'quit' to exit.\n")

    while True:
        user_message = input("Customer: ")

        if user_message.lower() in ["quit", "exit", "bye"]:
            print("Agent: Thanks for reaching out. Have a great day!")
            break

        response = ask_agent(user_message)
        print("Agent:", response)

run_agent()