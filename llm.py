import os
from dotenv import load_dotenv
import google.generativeai as genai

# .env file load karo
load_dotenv()

# API key lo
api_key = os.getenv("GEMINI_API_KEY")

# Gemini configure karo
genai.configure(api_key=api_key)

# Model select karo
model = genai.GenerativeModel("gemini-2.5-flash")

# Test
#response = model.generate_content("Hello! Who are you?")

#print(response.text)