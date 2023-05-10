import os
import json
import random

# Save messages for retrieval later on


def get_recent_messages():

    # Define the file name
    file_name = "stored_data.json"
    learn_instruction = {"role": "system",
                         "content": "You are a Insuarance Contracts Advisor, the user is called Peter. Peter is 62 years old and has long been working as a cashier and stock clerk in the local supermarket chain. Five years ago Peter suffered a stroke and he has since some difficulty concentrating and remembering things. He has therefore decided to pre-retire from his work and travel abroad along with his wife. In order to be safe he decided to contract a travel insurance. His Needs are as follows: Simple and summarized travel insurance information to consult before the travel, Quickly find and understand what is included and what is excluded, Quickly find what to do and who to contact in case of emergency during the travel, Simple way to access all the information above. His Fears and Frustrations: Long documents with complex legal language stress him and he becomes nervous until find and understand what he needs, He is stressed about not remembering where the physical or digital copies of his documents are stored. His Tech profile: Avid messaging and video call apps user, occasional social media apps and website user. Keep responses under 20 words. "}

    # Initialize messages
    messages = []

    # Add Random Element
    # x = random.uniform(0, 1)
    # if x < 0.2:
    #     learn_instruction["content"] = learn_instruction["content"] + \
    #         "Your response Facts about AXA's Motor Contracts "
    # elif x < 0.5:
    #     learn_instruction["content"] = learn_instruction["content"] + \
    #         "Your response must add humor and simple languge"
    # else:
    #     learn_instruction["content"] = learn_instruction["content"] + \
    #         "Your response will sincere "

    # Append instruction to message
    messages.append(learn_instruction)

    # Get last messages
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)

            # Append last 5 rows of data
            if data:
                if len(data) < 5:
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-5:]:
                        messages.append(item)
    except:
        pass

    # Return messages
    return messages


# Save messages for retrieval later on
def store_messages(request_message, response_message):

    # Define the file name
    file_name = "stored_data.json"

    # Get recent messages
    messages = get_recent_messages()[1:]

    # Add messages to data
    user_message = {"role": "user", "content": request_message}
    assistant_message = {"role": "assistant", "content": response_message}
    messages.append(user_message)
    messages.append(assistant_message)

    # Save the updated file
    with open(file_name, "w") as f:
        json.dump(messages, f)


# Save messages for retrieval later on
def reset_messages():

    # Define the file name
    file_name = "stored_data.json"

    # Write an empty file
    open(file_name, "w")
