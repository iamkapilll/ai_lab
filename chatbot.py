# simple_chatbot.py

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Simple responses based on user input
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but thanks for asking! How can I help you?"
    elif "what is your name" in user_input:
        return "I am a simple chatbot created to assist you."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def main():
    print("Welcome to the Simple Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)

        if user_input.lower() == "bye":
            break

if __name__ == "__main__":
    main()
