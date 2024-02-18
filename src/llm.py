import google.generativeai as genai
from prompt import system_instruction
# API_KEY = "AIzaSyAezKZT5ODtVc6bczVqg2FWQZ2YSIerbbY"
from dotenv import load_dotenv
import os
load_dotenv()

history = [
    {"role": "model", "text": system_instruction}
]

def ask_order(history):
    genai.configure(api_key=os.getenv('api_key'))
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(history)
    return response.text
