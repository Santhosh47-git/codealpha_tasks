def get_bot_response(user_input):
   
    user_input = user_input.lower().strip()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm doing great! How about you?"
    
    elif "your name" in user_input:
        return "I'm 'SimpleBot.' I don't have a last name yet!"
    
    elif "time" in user_input:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a productive day!"
    
    else:
        return "I'm sorry, I don't quite understand that. Could you try asking something else?"

def main():
    print("--- Welcome to SimpleBot ---")
    print("(Type 'bye' to exit the chat)\n")

    while True:
      
        user_text = input("You: ")
        
        response = get_bot_response(user_text)
        
        print(f"Bot: {response}")
        
        if "goodbye" in response.lower() or "bye" in response.lower():
            break

if __name__ == "__main__":

    main()
