#NLTK (Natural Language Toolkit) is a powerful library for working with human language data and Many developers really like using this platform to make chatbots
import nltk
from nltk.chat.util import Chat, reflections
'''This is a list of patterns and their corresponding responses
Each pattern is a tuple containing a regular exp. and a list of possible resp. so that
The regular expressions are used to match user input for basic question/answers '''
patterns = [
    (r'hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']),
    (r'how are you', ['I am doing well, thank you!', 'I\'m good. How about you?']),
    (r'fine|good', ['That\'s great!', 'Awesome!', 'Good to hear!']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
    (r'what\'s your name', ['I am a chatbot.', 'You can call me a bot']),
    (r'your favorite color', ['I don\'t have a favorite color. I\'m a text-based entity.']),
    (r'how old are you', ['I don\'t have an age. I\'m just a computer program.']),
    (r'where are you from', ['I exist in the digital realm, so I don\'t have a specific location.but recently my developer got shifted in New Delhi from Haryana']),
    (r'tell me a joke', ['Why did the computer go to therapy? It had too many bytes of emotional baggage!']),
    (r'who created you', ['I was created by a 1st year student who also known as KC']),
    (r'favorite book', ['I don\'t read books, but I can recommend some if you tell me your preferences.']),
    (r'weather', ['I don\'t have real-time information. You can check a weather website for the latest updates.']),
    (r'how to learn programming', ['Learning programming is best done through practice. Start with a beginner-friendly language like Python.']),
    (r'favorite movie', ['I don\'t watch movies, but I can suggest popular ones if you tell me your taste.']),
    (r'programming languages', ['There are many programming languages like Python, Java, and C++. Each has its strengths and use cases.']),
    (r'what do you do', ['I\'m here to chat with you and answer your basic questions.']),
    (r'tell me about yourself', ['I am a text-based chatbot created by KC.']),
    (r'how can I contact you', ['I don\'t have personal contact information. You can interact with me here.']),
    (r'favorite food', ['I don\'t eat, so I don\'t have a favorite food.']),
    (r'are you human', ['No, I am a machine learning model created by KC.']),
    (r'(.*)', ['I\'m not sure I understand. Can you please rephrase that?', 'I didn\'t get that. I just understand some regular expressions only']),
]
chatbot = Chat(patterns, reflections) # The Chat() class from NLTK is used to create a chatbot instance. It takes the patterns and reflections as params.
'''This func initializes the chat with a greeting. 
It then enters a loop where it continuously takes user input using a True statement until user say "bye"
Otherwise, it uses the respond method of the chatbot to generate a basic response and prints it'''
def start(): 
    print("Hello!! I am your ChAt_BoT.Type 'bye' to exit")
    while True:
        user = input("You: ")
        if user.lower() == 'bye':
            print("Goodbye!")
            break
        else:
            response = chatbot.respond(user)
            print("ChAt_Bot:", response)
start()
