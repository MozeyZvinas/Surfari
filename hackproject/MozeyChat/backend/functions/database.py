import os
import json
import random

# Save messages for retrieval later on


def get_recent_messages():

    # Define the file name
    file_name = "stored_data.json"
    learn_instruction = {"role": "system",
                         "content": "You are a Insuarance Contracts Advisor, the user is called Peter. Peter is 62 years old and has long been working as a cashier and stock clerk in the local supermarket chain. Five years ago Peter suffered a stroke and he has since some difficulty concentrating and remembering things. He has therefore decided to pre-retire from his work and travel abroad along with his wife. In order to be safe he decided to contract a travel insurance. His Needs are as follows: Simple and summarized travel insurance information to consult before the travel, Quickly find and understand what is included and what is excluded, Quickly find what to do and who to contact in case of emergency during the travel, Simple way to access all the information above. His Fears and Frustrations: Long documents with complex legal language stress him and he becomes nervous until find and understand what he needs, He is stressed about not remembering where the physical or digital copies of his documents are stored. His Tech profile: Avid messaging and video call apps user, occasional social media apps and website user. Here is some of AXA's Contract: Policy Summary: COVERWISE BRONZE - AXA Travel Insurance: This policy summary does not contain full details and conditions of your insurance – these are located in your policy wording. This insurance is underwritten by Inter Partner Assistance (S.A.) apart from Section L - Scheduled airline failure which is provided by International Passenger Protection Limited, IPP House, 22-26 Station Road, West Wickham, Kent, BR4 0PR, United Kingdom (“IPP’’) and Underwritten by certain Underwriters at Lloyds whose details are shown under the Special definitions relating to Section L - Scheduled airline failure. Where a heading is underlined in this policy summary full details can be found in your policy wording under the same heading. Type of insurance and cover: Travel insurance for single or annual multi trips – Please refer to your policy schedule for your selected cover.Age eligibility: If annual multi trip is selected, this policy is not available to anyone aged 66 or over. If you are aged under 18 (or aged under 23 if in full-time education) you are only insured when traveling with one or both of the insured adults or traveling with parental permission. If you reach any of the ages mentioned above during the period of insurance, cover will continue until the next renewal date but not after that. If single trip cover is selected, this policy is not available to anyone aged 76 or over. Conditions: It is essential that you refer to the Important conditions relating to health in the policy wording, as failure to comply with these conditions may jeopardize your claim or cover. If you are traveling to Australia and you require medical treatment, you must enroll with a local Medicare office. Special conditions apply to each section of your policy - Please refer to the policy wording for full details. Significant features and benefits: War risks, civil commotion, and terrorism – cover for these events is provided under Section B – Emergency medical and other expenses (unless caused by nuclear, chemical, or biological attack) – Please see paragraph 1. in the What is not covered - applicable to all sections of the policy in the policy wording for full details. The table shows the maximum amount payable for each insured person after the deduction of the policy excess (unless otherwise stated). Some sections are optional and these are marked* - your policy schedule will show if you selected any of these options. Please note that the cover under Section L – Scheduled airline failure is not underwritten by Inter Partner Assistance (S.A.) but by certain Underwriters at Lloyds. Please see the section for further details. Section	Title	Limit	Excess: A	Cancellation or curtailment charges	£1,500	£100; B	Emergency medical and other expenses	£10,000,000	£100; Emergency dental treatment	£200	£100; C	Personal accident	£10,000	Nil. Page 2: COVERWISE BRONZE - AXA Travel Insurance. Section D: Baggage, Title	Limit	Excess, Baggage	£1,500	£100, Single article limit	£200	£100, Total for all valuables	£200	£100. Section E: Personal money, passport and documents, Title	Limit	Excess, Personal money, passport and documents	£200 cash (£50 if under 16) and £100 other money and documents	£100, Travel and accommodation costs for replacement passport	£150	Nil. Section F: Personal liability, Title	Limit	Excess, Personal liability	£2,000,000	£200. Section G*: Ski equipment, Title	Limit	Excess, Ski equipment	£300	£100, Single article limit for own ski equipment	£150	£100. Hired ski equipment	£200	£100. Section H*: Ski equipment hire. Title	Limit	Excess. Ski equipment hire	£150 (£15 per day)	Nil. Section I*: Ski pack. Title	Limit	Excess. Ski pack	£200	Nil. Lost lift pass	£150	Nil. Section J*: Piste closure, Title	Limit	Excess, Piste closure	£150 (£15 per day)	Nil. Section K*: Avalanche or landslide cover Title	Limit	Excess. Avalanche or landslide cover	£200 (£15 per day)	Nil. Section L: Scheduled airline failure (not applicable to single trip policies) Title,	Limit,	Excess. Scheduled airline failure	£1,500	Nil. Significant or unusual limitations or what is not covered. You not accurately answering any question(s) we have asked you at the time of buying this insurance, where your answer(s) may have affected our decision to provide you with this policy.The standard excess you have agreed to pay will be shown within your policy wording or on the policy schedule. Under annual multi-trip policies, there is no cover for trips over 24 days. Any trip that had already begun when you purchased this insurance will not be covered, except where this policy replaces or you renew an existing annual Coverwise multi-trip policy which fell due for renewal during the trip. What is not covered applicable to all sections of the policy: War risks, civil commotion, terrorism (except under Section B – Emergency medical and other expenses unless caused by nuclear, chemical or biological attack), sonic bangs, radioactive contamination.There are a number of sports, activities, and winter sports that are not covered - Please see paragraphs 4, 5, and 6 in the What is not covered - applicable to all sections of the policy in the policy wording. Climbing on or jumping from vehicles, buildings, or balconies regardless of the height. Wilful, self-inflicted injury, suicide, drug use, or solvent abuse. You drinking too much alcohol, resulting in a claim. Unlawful actions and any criminal proceedings brought against you. Travel to a country, specific area, or event which the Foreign and Commonwealth Office or the World Health Organization has advised against all travel or all but essential travel. What is not covered under Section A – Cancellation or curtailment charges:Redundancy caused by misconduct, resignation, voluntary redundancy, or where you received a warning or notification of redundancy before you purchased this insurance or at the time of booking any trip. Any circumstances known to you before you purchased this insurance or at the time of booking any trip that could reasonably be expected to result in a claim. Keep responses under 20 words. What is not covered under Section B – Emergency medical and other expenses: Medical expenses that are not considered customary and/or reasonable in the country in which the treatment is administered. Any tests, treatment, or surgery which, in the opinion of the Emergency Assistance Service or us (based on information provided by the medical practitioner in attendance), can be reasonably delayed until your return to your home area. Treatment or surgery which, in the opinion of the Emergency Assistance Service, can wait until your return to your home area. Medication, which prior to departure is known to be required.Expenses incurred as a result of a tropical disease where the NHS recommended inoculations have not been undertaken and/or the NHS recommended medication has not been taken.What is not covered under Section D – Baggage: Valuables left unattended at any time unless in a hotel safe, safety deposit box, or in your locked accommodation.Baggage contained in an unattended vehicle between 9 pm and 9 am (or at any time between 9 am and 9 pm unless it is locked out of sight in a secure baggage area) – Please see the definition of secure baggage area in the Definitions in the policy wording. Contact or corneal lenses, hearing aids, dental or medical fittings, ski equipment, golf equipment, and other items are excluded - See your policy wording for the full list. Business goods, samples, or tools used in connection with your occupation. Mobile phones of any kind. What is not covered under Section E – Personal money, passport, and documents Personal money or your passport or visa left unattended at any time unless in a hotel safe, safety deposit box, or in your locked accommodation.Loss or theft of traveler's cheques where you have not complied with the issuing agents' conditions.What is not covered under Section F – Personal liability: Pursuit of any trade, business, or profession, or the ownership, possession, or use of mechanically propelled vehicles, aircraft, or watercraft. What is not covered under Sections G, H, I, J & K – Winter sports: Ski equipment contained in or stolen from an unattended vehicle between 9 pm and 9 am (or at any time between 9 am and 9 pm unless it is locked out of sight in a secure baggage area) – Please see the definition of secure baggage area in the Definitions in the policy wording. A deduction for wear, tear, and depreciation will be made on ski equipment – see the table in Section G – Ski equipment.The closure or impending closure of the skiing facilities in your resort existing or being publicly announced by the date you purchased this insurance or at the time of booking any trip. Cancellation period: You are free to cancel this policy at any time. If you wish to cancel within 14 days of receipt of the policy documents, you may by writing to us for a full refund providing you have not traveled and no claim has been made. If you cancel after the first 14 days of receipt of the documents, no premium refund will be made. See General conditions applicable to the whole policy in the policy wording for full details. Claim notification: To make a claim, contact: 0330 024 8315 or Scheduled airline failure where you should contact: 0208 776 3752 (annual multi-trip policies only)."}

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
            "You response must have some light humor"

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
