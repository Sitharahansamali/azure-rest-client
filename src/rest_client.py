import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

AZURE_ENDPOINT = os.getenv("AI_SERVICE_ENDPOINT")
AZURE_KEY = os.getenv("AI_SERVICE_KEY")
ANALYZE_PATH = "/text/analytics/v3.1/languages"

def detect_language(text):
    url = AZURE_ENDPOINT + ANALYZE_PATH
    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_KEY,
        "Content-Type": "application/json"
    }
    body = {
        "documents": [
            {"id": "1", "text": text}
        ]
    }

    response = requests.post(url, headers=headers, json=body)
    if response.status_code != 200:
        print(f"Error: {response.status_code}, {response.text}")
        return

    data = response.json()
    doc = data['documents'][0]
    language = doc['detectedLanguage']['name']
    confidence = doc['detectedLanguage']['confidenceScore']

    print(f"Document Id: {doc['id']}")
    print(f"Detected Language: {language}")
    print(f"Confidence Score: {confidence}")

if __name__ == "__main__":
    text = input("Enter text to analyze: ")
    detect_language(text)