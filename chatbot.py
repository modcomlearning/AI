import random
import re

# Dictionary of responses
responses = {
    r'hi|hello|hey': ['Hello!', 'Hey there!', 'Hi!'],
    r'bye|goodbye': ['Goodbye!', 'Bye!', 'Have a nice day!'],
    r'teachers|faculty': ['We have a great team of teachers at our school.'],
    r'courses|classes': ['We offer a variety of courses.'],
    r'location|where': ['Our school is located at 123 School St, City.'],
    r'hours|timing': ['School hours are from 8 AM to 3 PM, Monday through Friday.'],
    r'help|information': ['How can I assist you?', 'What do you need help with?'],
    r'(.*)': ['Please ask something else.', 'Im sorry, I dont understand.']
}

def respond(message):
    for pattern, responses_list in responses.items():
        if re.search(pattern, message, re.IGNORECASE):
            return random.choice(responses_list)
    return random.choice(responses[r'(.*)'])

print("School Chatbot: Hi! How can I help you today? (type 'exit' to quit)")

while True:
    user_message = input("You: ").lower()
    
    if user_message == 'exit':
        print("School Chatbot: Goodbye!")
        break
    
    bot_response = respond(user_message)
    print("School Chatbot:", bot_response)
