import os
import requests
from pathlib import Path
from dotenv import load_dotenv
from django.http import JsonResponse

dotenv_path = Path("project/.env")
load_dotenv(dotenv_path=dotenv_path)
APIENV = os.getenv("BLACK_HISTORY_API_KEY")

# length is the max character length of the returned quote
url = "https://rest.blackhistoryapi.io/fact/random?length=164"
headers = {
    "x-api-key":APIENV
}

# function to make a GET request to the Black History Facts API
def get_fact(request):
    response = requests.get(url, headers=headers)
    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the JSON response to extract the quote
        data = response.json()
        # quote = data["q"]
        # author = data["a"]
        # print(data)
        # return JsonResponse(data)
        return JsonResponse(data)
    else:
        print("Error: Unable to retrieve quote")
