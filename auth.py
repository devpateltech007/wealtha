from dotenv import load_dotenv
import requests
import os
load_dotenv()

# Replace these with your actual API key and secret
API_KEY_ID = os.environ['ALPACA_API_KEY']
API_SECRET_KEY = os.environ['ALPACA_API_SECRET_KEY']

# Define the headers
headers = {
    "APCA-API-KEY-ID": API_KEY_ID,
    "APCA-API-SECRET-KEY": API_SECRET_KEY
}

# Send a GET request
url = f"https://paper-api.alpaca.markets/v2/account"
response = requests.get(url, headers=headers)
adsdasdas
# Print the response
print(response.status_code)
print(response.json())
