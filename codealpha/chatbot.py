# Basic Rule-Based Chatbot

def chatbot():
    print("🤖 ChatBot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("🤖 ChatBot: Hi!")
        
        elif user == "how are you":
            print("🤖 ChatBot: I'm fine, thanks!")
        
        elif user == "what is your name":
            print("🤖 ChatBot: I am a simple Python ChatBot.")
        
        elif user == "bye":
            print("🤖 ChatBot: Goodbye!")
            break
        
        else:
            print("🤖 ChatBot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()