from memory import add_message, get_history
from llm import model

print("🤖 AI Chatbot")
print("Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")
    add_message("User: " + user_input)

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = model.generate_content(user_input)

    print("AI:", response.text)
    
    add_message("AI: " + response.text)
    
    print(get_history())