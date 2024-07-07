import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'bye|goodbye', ['Goodbye!', 'Bye!', 'Have a nice day!']),
    (r'how are you', ['I am good, thank you.', 'Fine, and you?', 'I am doing well.']),
    (r'(.*) (teachers|faculty)', ['We have a great team of teachers at our school.']),
    (r'(.*) (courses|classes)', ['We offer a variety of courses.Python, HTML etc']),
    (r'(.*) (location|where)', ['Our school is located at 123 School St, City.']),
    (r'(.*) (hours|timing)', ['School hours are from 8 AM to 3 PM, Monday through Friday.']),
    (r'(.*)', ['Please ask something else.', 'I\'m sorry, I don\'t understand.'])
]

# Create chatbot
chatbot = Chat(patterns, reflections)

# Main interaction loop
print("School Chatbot: Hi! How can I help you today? (type 'exit' to quit)")

while True:
    user_input = input("You: ").lower()
    
    if user_input == 'exit':
        print("School Chatbot: Goodbye!")
        break
    
    response = chatbot.respond(user_input)
    print("School Chatbot:", response)
