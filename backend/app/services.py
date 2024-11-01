# app/services.py

import os
import requests

# Load environment variables
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")

def get_word_meaning(word):
    """Fetch the meaning of the word from the OpenAI API."""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPEN_AI_KEY}",
        "Content-Type": "application/json",
    }

    # Create the prompt for OpenAI
    prompt = f"Provide a short meaning for the word '{word}'. Don't give anything else, be clear"
    data = {
        "model": "gpt-3.5-turbo",  # Adjust the model as necessary
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 50,  # Adjust as necessary for your response length
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        return response_data['choices'][0]['message']['content'].strip()  # Return the meaning
    else:
        print(f"Error fetching meaning: {response.status_code} - {response.text}")
        return None  # Return None if there's an error


def get_example_usage(word):
    """Fetch an example usage of the word from the OpenAI API."""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPEN_AI_KEY}",
        "Content-Type": "application/json",
    }

    # Create the prompt for OpenAI
    prompt = f"Provide a short example sentence using the word '{word}'.Don't give anything else, be clear"
    data = {
        "model": "gpt-3.5-turbo",  # Adjust the model as necessary
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 50,  # Adjust as necessary for your response length
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        return response_data['choices'][0]['message']['content'].strip()  # Return the example
    else:
        print(f"Error fetching example: {response.status_code} - {response.text}")
        return None  # Return None if there's an error
