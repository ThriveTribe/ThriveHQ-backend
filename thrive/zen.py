import os
import requests
from pathlib import Path
from dotenv import load_dotenv
from django.http import JsonResponse

# function to make a GET request to the ZenQuotes API
def get_zen(request):
    response = requests.get("https://zenquotes.io/api/today/")
    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the JSON response to extract the quote
        data = response.json()[0]
        # quote = data["q"]
        # author = data["a"]
        # print(f"{quote} - {author}")
        return JsonResponse(data)
    else:
        print("Error: Unable to retrieve quote")
