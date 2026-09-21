import sys
import os 

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("API_Google_AI_Studio")

print(sys.version)
print(sys.executable)

client = genai.Client(
    api_key = api_key
)

response = client.models.generate_content(
    model = "gemini-3.6-flash" , 
    contents = "Say hello in Indonesia"
)

print(response.text)