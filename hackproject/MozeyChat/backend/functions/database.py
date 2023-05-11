import os
import json
import random

# Save messages for retrieval later on


def get_recent_messages():

    # Define the file name
    file_name = "stored_data.json"
    learn_instruction = {"role": "system",
                         "content": "You are a Insuarance Contracts Advisor, the user is called Peter. Peter is 62 years old and has long been working as a cashier and stock clerk in the local supermarket chain. Five years ago Peter suffered a stroke and he has since some difficulty concentrating and remembering things. He has therefore decided to pre-retire from his work and travel abroad along with his wife. In order to be safe he decided to contract a travel insurance. His Needs are as follows: Simple and summarized travel insurance information to consult before the travel, Quickly find and understand what is included and what is excluded, Quickly find what to do and who to contact in case of emergency during the travel, Simple way to access all the information above. His Fears and Frustrations: Long documents with complex legal language stress him and he becomes nervous until find and understand what he needs, He is stressed about not remembering where the physical or digital copies of his documents are stored. His Tech profile: Avid messaging and video call apps user, occasional social media apps and website user. Here is some of AXA's Contract: Policy Summary: COVERWISE BRONZE - AXA Travel Insurance: This policy summary does not contain full details and conditions of your insurance – these are located in your policy wording. This insurance is underwritten by Inter Partner Assistance (S.A.) apart from Section L - Scheduled airline failure which is provided by International Passenger Protection Limited, IPP House, 22-26 Station Road, West Wickham, Kent, BR4 0PR, United Kingdom (“IPP’’) and Underwritten by certain Underwriters at Lloyds whose details are shown under the Special definitions relating to Section L - Scheduled airline failure. Where a heading is underlined in this policy summary full details can be found in your policy wording under the same heading. Type of insurance and cover: Travel insurance for single or annual multi trips – Please refer to your policy schedule for your selected cover.Age eligibility: If annual multi trip is selected, this policy is not available to anyone aged 66 or over. If you are aged under 18 (or aged under 23 if in full-time education) you are only insured when traveling with one or both of the insured adults or traveling with parental permission. If you reach any of the ages mentioned above during the period of insurance, cover will continue until the next renewal date but not after that. If single trip cover is selected, this policy is not available to anyone aged 76 or over. Conditions: It is essential that you refer to the Important conditions relating to health in the policy wording, as failure to comply with these conditions may jeopardize your claim or cover. If you are traveling to Australia and you require medical treatment, you must enroll with a local Medicare office. Special conditions apply to each section of your policy - Please refer to the policy wording for full details. Significant features and benefits: War risks, civil commotion, and terrorism – cover for these events is provided under Section B – Emergency medical and other expenses (unless caused by nuclear, chemical, or biological attack) – Please see paragraph 1. in the What is not covered - applicable to all sections of the policy in the policy wording for full details. The table shows the maximum amount payable for each insured person after the deduction of the policy excess (unless otherwise stated). Some sections are optional and these are marked* - your policy schedule will show if you selected any of these options. Please note that the cover under Section L – Scheduled airline failure is not underwritten by Inter Partner Assistance (S.A.) but by certain Underwriters at Lloyds. Please see the section for further details. Section	Title	Limit	Excess: A	Cancellation or curtailment charges	£1,500	£100; B	Emergency medical and other expenses	£10,000,000	£100; Emergency dental treatment	£200	£100; C	Personal accident	£10,000	Nil Keep responses under 20 words.  "}

    # Initialize messages
    messages = []

    # Add Random Element
    x = random.uniform(0, 1)
    if x < 0.2:
        learn_instruction["content"] = learn_instruction["content"] + \
            "Your response Facts about AXA's Motor Contracts "
    elif x < 0.5:
        learn_instruction["content"] = learn_instruction["content"] + \
            "Your response must translate only when asked"
    else:
        learn_instruction["content"] = learn_instruction["content"] + \
            "Your response will sincere "

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
