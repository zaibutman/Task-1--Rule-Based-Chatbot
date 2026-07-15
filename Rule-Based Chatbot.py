# ==========================================================
# Project 1: Rule-Based AI Chatbot
# Name: Zaib Utman
# Internship: Artificial Intelligence Intern
# Organization: Decode Labs
# ==========================================================

# Welcome Message
print("=" * 60)
print("🤖 Welcome to the Rule-Based AI Chatbot!")
print("I can answer basic questions.")
print("Type 'bye', 'exit', or 'quit' to end the conversation.")
print("=" * 60)

# Dictionary containing chatbot responses
responses = {
    "hello": "Hi! How can I help you today?",
    "hi": "Hello! Nice to meet you.",
    "hey": "Hey! How's it going?",
    "good morning": "Good morning! Have a wonderful day.",
    "good afternoon": "Good afternoon!",
    "good evening": "Good evening!",

    "how are you": "I'm doing great! Thanks for asking.",
    "who are you": "I'm a Rule-Based AI Chatbot created using Python.",
    "what is your name": "My name is DecodeBot.",
    "what can you do": "I can answer basic predefined questions.",

    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine Learning is a branch of AI that enables computers to learn from data.",
    "what is python": "Python is a popular programming language used in AI, Machine Learning, and Web Development.",

    "thank you": "You're welcome!",
    "thanks": "My pleasure!",
    "help": "Try asking me about AI, Python, or greet me with hello."
}

# Continuous conversation loop
while True:

    # Take user input
    user = input("\nYou: ").lower().strip()

    # Exit condition
    if user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day. 😊")
        break

    # Search for response
    response = responses.get(
        user,
        "Sorry, I don't understand that. Please try another question."
    )

    # Display chatbot response
    print("Bot:", response)