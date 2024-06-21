import nltk
from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses.
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by ChatGPT. You can call me Chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem",]
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Nice to hear that!", "Alright, great!",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon!",]
    ],
    [
        r"(.*)",
        ["That's interesting!", "Tell me more!", "I see.", "Could you elaborate?", "Why do you say that?", "How do you feel about that?"]
    ],
]

def chatbot():
    print("Hi, I'm your chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.download('punkt')  # Download the punkt tokenizer data if not already downloaded
    chatbot()
