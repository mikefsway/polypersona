from openai import OpenAI
import pandas as pd
import numpy as np
import csv
import os
import json

# Example CSV file reading (adjust the path and structure as needed)
df = pd.read_csv('demoprobs.csv')
i = 1
# Assume df structure like:
#   Gender, Probability, AgeGroup, Probability, ...
#   Male, 0.5, 0-18, 0.2, ...
#   Female, 0.5, 19-35, 0.3, ...

def select_demographic_state(characteristic):
    """
    Selects a state for a demographic characteristic based on probabilities.
    :param characteristic: The demographic characteristic (e.g., 'Gender').
    :return: The selected state (e.g., 'Male' or 'Female').
    """
    states = df[characteristic].dropna().tolist()
    probabilities = df['prob_' + characteristic].dropna().tolist()
    return np.random.choice(states, p=probabilities)

def run_query():    # Example usage

    gender = select_demographic_state('gender')
    age = select_demographic_state('age')
    env_conc = select_demographic_state('env_conc')
    income = select_demographic_state('income')
    household = select_demographic_state('household')
    education = select_demographic_state('education')
    occupancy = select_demographic_state('occupancy')
    tenure = select_demographic_state('tenure')
    risk = select_demographic_state('risk')
    trust = select_demographic_state('trust')
    place = select_demographic_state('place')
    innovation = select_demographic_state('innovation')
    economic = select_demographic_state('economic')
    politics = select_demographic_state('politics')
    extraversion = select_demographic_state('extraversion')
    agreeableness = select_demographic_state('agreeableness')
    conscientiousness = select_demographic_state('conscientiousness')
    neuroticism = select_demographic_state('neuroticism')
    openess = select_demographic_state('openess')
    time = select_demographic_state('time')
    proportion = select_demographic_state('proportion')
    scale = select_demographic_state('scale')
    operator = select_demographic_state('operator')
    
    global i 
    print(f"Run number {i}")

    system_msg = f"You are a UK householder completing a survey {time}. You are {gender}, aged {age}, with a {income} household income, {household} people in your household, you highest level of education is '{education}', you {occupancy}, and you are a {tenure}. You have these attitudes: {env_conc} environmental concern, {risk} risk aversion, {trust} social trust, {politics} politics, {place} place attachment, {economic} economic rationality, and your innovation adoption status is '{innovation}'. Your personality has traits of {extraversion} extraversion, {agreeableness} agreeableness, {conscientiousness} conscientiousness, {neuroticism} neuroticism, and {openess} openess to new experience."

    user_msg = f"A new energy offer is available which allows you to buy energy directly from homes and businesses with their own solar panels. Energy bought this way is slightly cheaper than what you get from your usual supplier. If you participate, you could meet around {proportion} of your household’s electricity needs through the offer. You would buy electricity directly from homes and businesses located {scale}. You would continue to buy the rest of your energy from your current supplier. Would you sign up to participate in this offer if it was available to you today? Provide your response in JSON. The first JSON object should be a short (<50 word) explanation of your reasoning, called 'explanation', drawing on your demographic, attitudinal, and personality characteristics. Then, output your decision on whether or not you would participate, in a JSON object called 'decision', with response options yes=1 or no=0 (return an integer). Your decision must be consistent with your explanation. Example output as follows: 'explanation': 'explanation text here', 'decision': integer"

    print(system_msg)
    print(f"{scale}, {proportion}")

    client = OpenAI()

    try:
        completion = client.chat.completions.create(
            # model="gpt-4-1106-preview",
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg}
            ]
        )

        response_text = completion.choices[0].message.content
        print(response_text)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # Handle any other unexpected errors
        response_text = "Default response due to unexpected error"

        # Assuming response_text is a JSON string
    response_json = json.loads(response_text)

        # Add the additional variable values to the JSON data
    response_json.update({
        'gender': gender,
        'age': age,
        'env_conc': env_conc,
        'income': income,
        'household': household,
        'education': education,
        'occupancy': occupancy,
        'tenure': tenure,
        'risk': risk,
        'trust': trust,
        'place': place,
        'innovation': innovation,
        'economic': economic,
        'politics': politics,
        'extraversion': extraversion,
        'agreeableness': agreeableness,
        'conscientiousness': conscientiousness,
        'neuroticism': neuroticism,
        'openess': openess,
        'time': time
    })

    print(response_json)

    # Define the CSV file name
    csv_file = 'p2p_rep_data.csv'

    # Check if the file exists
    file_exists = os.path.isfile(csv_file)

    # Open the file in append mode, create it if it doesn't exist
    with open(csv_file, mode='a', newline='') as file:
        # Define the fieldnames based on the JSON keys
        fieldnames = response_json.keys()

        # Create a CSV DictWriter object
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header only if the file is being created
        if not file_exists:
            writer.writeheader()

        # Write the JSON data as a row in the CSV file
        writer.writerow(response_json)

    print("Data saved to CSV successfully.")

    i = i + 1

while i<2:
    run_query()

