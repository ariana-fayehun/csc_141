# I applied what I learned in the text to figure out how to complete this 
# assignment

# List that defines a bunch of messages and an empty list that defines a list
# of sent messages. It starts out empty
messages = ['Hello!', 'How are you?', "I'm fine, you?"]
sent_messages = []

def send_messages():
    '''Prints all the messages in a loop, removes them from messages, and
    appends them to sent_messages'''
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

# Runs the function and prints the lists
send_messages()
print(messages)
print(sent_messages)