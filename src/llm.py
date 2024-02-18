import google.generativeai as genai
from src.prompt import system_instruction
API_KEY = "AIzaSyAezKZT5ODtVc6bczVqg2FWQZ2YSIerbbY"
from dotenv import load_dotenv
import os
load_dotenv()

history = [
    {"text": system_instruction,"role": "user"}
]

def ask_order(message):
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    response=chat.send_message(system_instruction)
    response=chat.send_message(message)
    return response.text
