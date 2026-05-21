# Simple Customer Service AI Agent

faq = {
    "hours": "We are open Monday to Friday from 9 AM to 5 PM.",
    "refund": "Refunds are available within 30 days with a receipt.",
    "shipping": "Standard shipping takes 3–5 business days.",
    "contact": "You can contact support at support@example.com.",
    "price": "Our pricing depends on the service. Please tell me what you're interested in.",
    "location": "We are located in South San Francisco, CA."
}

def find_answer(user_message):
    user_message = user_message.lower()

    for keyword, answer in faq.items():
        if keyword in user_message:
            return answer

    return "I'm not sure yet, but I can connect you with a human support rep."

def run_agent():
    print("Customer Service Agent")
    print("Type 'quit' to exit.\n")

    while True:
        user_message = input("Customer: ")

        if user_message.lower() in ["quit", "exit", "bye"]:
            print("Agent: Thanks for reaching out. Have a great day!")
            break

        response = find_answer(user_message)
        print("Agent:", response)

run_agent()