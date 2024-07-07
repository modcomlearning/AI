#random: This module is imported to help select random responses from the list of possible responses.
#re: This module provides support for working with regular expressions in Python, which is used to match patterns in user input.
import random
import re

#responses: This dictionary holds various regular expressions as keys and corresponding lists of responses as values. Each key represents a regular expression pattern, and its value is a list of possible responses that the chatbot can give when a message matches that pattern.
# For instance, r'hi|hello|hey' matches variations of greetings and provides a list of greeting responses.

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
    # Add more training data
}

# respond function: This function takes a message as input, which is the user's input message.
# It iterates through each key-value pair in the responses dictionary using responses.items().
# For each pair, it checks if the message matches the regular expression pattern using re.search(). The re.IGNORECASE flag is used to make the pattern matching case-insensitive.
# If a match is found, it randomly selects and returns one of the responses from responses_list.
# If no specific pattern matches (for pattern, responses_list in responses.items()), it falls back to the generic response defined by responses[r'(.*)'], which handles any other input.


def respond(message):
    for pattern, responses_list in responses.items():
        if re.search(pattern, message, re.IGNORECASE):
            return random.choice(responses_list)
    return random.choice(responses[r'(.*)'])

print("School Chatbot: Hi! How can I help you today? (type 'exit' to quit)")


#The program starts by printing a welcome message and instructions for the user.
#It then enters a while True loop to continuously prompt the user for input (user_message).
#If the user types 'exit', the program prints a goodbye message and breaks out of the loop, terminating the program.
#Otherwise, it calls the respond function with user_message to generate a response (bot_response) based on the input.
#Finally, it prints the bot's response to the console.


while True:
    user_message = input("You: ").lower()
    
    if user_message == 'exit':
        print("School Chatbot: Goodbye!")
        break
    
    bot_response = respond(user_message)
    print("School Chatbot:", bot_response)
