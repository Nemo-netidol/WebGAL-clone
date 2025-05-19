import requests
from dotenv import load_dotenv
import os
from openai import OpenAI


load_dotenv()


API_KEY = os.environ.get("API_KEY")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=API_KEY,
)

api_key = API_KEY
API_URL = 'https://openrouter.ai/api/v1/chat/completions'

# Define the headers for the API request
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Define the request payload (data)

def _send_to_AI(user_input: str):
    data = {
        "model": "deepseek/deepseek-chat:free",
        "messages": [{"role": "user", "content": user_input}]
    }

    # Send the POST request to the DeepSeek API
    response = requests.post(API_URL, json=data, headers=headers)


    # Check if the request was successful
    if response.status_code == 200:
        response = response.json()['choices'][0]['message']['content']
        print("API Response:", response)
        with open('../scene/response.txt', "w") as file:
            response = f"Response: {response};"
            file.write(response)
        return {"status": "success", "generated": response}
    else:
        print("Failed to fetch data from API. Status Code:", response.status_code)
        return {"status": "fail", "not generated": response}


def generate_response_from_file(input_path: str) -> str:

    file =  open(input_path, "r")
    user_input = file.read()
    _send_to_AI(user_input)
    
    
def generate_response(user_input: str) -> str:
    _send_to_AI(user_input)

    