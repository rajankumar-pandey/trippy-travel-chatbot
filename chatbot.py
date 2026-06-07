import random
import re

def clean_input(user_text):
    return user_text.lower().strip()

def get_bot_response(user_message):
    def has_word(keywords, text):
        return any(re.search(rf"\b{word}\b", text) for word in keywords)

    if has_word(["hello", "hi", "hey"], user_message):
        return "Hey there! I'm Trippy, your virtual travel guide. Are you looking for a beach getaway, a mountain adventure, or just a good place to eat?"
    
    elif has_word(["beach", "sea", "sunny"], user_message):
        return "If you love sun and sand, I highly recommend Goa or the Maldives! Don't forget to pack your sunscreen."
    
    elif has_word(["mountain", "snow", "cold", "heights"], user_message):
        return "Craving the heights? You should check out Manali or the Swiss Alps. Perfect for trekking and hot cocoa!"
    
    elif has_word(["food", "eat", "restaurant", "cuisine"], user_message):
        return "A true traveler is always hungry! For incredible street food, check out Bangkok or Delhi. What kind of cuisine do you prefer?"
    
    elif has_word(["budget", "cheap", "cost"], user_message):
        return "Travel doesn't have to be expensive! Backpacking through Vietnam or Prague offers incredible views at a very low cost."
    
    elif has_word(["help", "what can you do"], user_message):
        return "I can help you pick your next destination! Just tell me if you prefer 'beaches', 'mountains', 'budget travel', or 'local food'."
    
    elif has_word(["bye", "exit", "quit"], user_message):
        return "Goodbye! Safe travels and catch you on your next adventure!"
    
    else:
        fallbacks = [
            "Hmm, that sounds interesting! Tell me more—are you leaning towards a beach trip or a mountain trek?",
            "I didn't quite catch that. Try asking me about 'beaches', 'mountains', or 'budget options'!",
            "Trippy is still learning! Could you rephrase that? Tell me what kind of holiday you are dreaming of."
        ]
        return random.choice(fallbacks)

def start_chatbot():
    print("==================================================")
    print("         TRIPPY: YOUR PERSONAL TRAVEL BOT         ")
    print("      (Type 'bye' or 'exit' to close the bot)     ")
    print("==================================================")
    
    while True:
        try:
            user_input = input("\nYou: ")
            processed_input = clean_input(user_input)
            
            if not processed_input:
                continue
                
            response = get_bot_response(processed_input)
            print(f"Trippy: {response}")
            
            if any(word in processed_input for word in ["bye", "exit", "quit"]):
                break
                
        except (KeyboardInterrupt, EOFError):
            print("\nTrippy: Exiting chat loop. Safe travels!")
            break

if __name__ == "__main__":
    start_chatbot()
