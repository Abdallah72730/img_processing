import os
from dotenv import load_dotenv

#load the dotenv file where the api keys are stored
load_dotenv()

#get the google api key
Google_api_key = os.getenv("GOOGLE_API_KEY")

#check if we have the api 
if not Google_api_key:
    print("No google api key found in the .env file")
    print("Please add the api key in the .env file")
    exit(1)