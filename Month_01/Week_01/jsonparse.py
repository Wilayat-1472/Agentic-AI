import os
import requests
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("API_BASE_URL")
url = f"{base_url}/posts"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses


    posts = response.json()
    for post in posts[:5]:
        print(f"Post ID: {post['id']}, Title: {post['title']}")

except requests.exceptions.RequestException as error:
    print(f"An error occurred: {error}")