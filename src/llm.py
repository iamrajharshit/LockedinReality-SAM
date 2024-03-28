import google.generativeai as genai
from src.prompt import system_instruction
API_KEY = "AIzaSyBPlccp4q2iMQ9ZSRIFR-yB-wzqRAGxHtk"
# from dotenv import load_dotenv
# import os
# load_dotenv()

history = [
    {"text": system_instruction,"role": "user"}
]

def ask_order(message):
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro',safety_settings=[
        {"category":'HARM_CATEGORY_HARASSMENT',
                             "threshold":'BLOCK_NONE'},
                            {"category":'HARM_CATEGORY_DANGEROUS_CONTENT',
                             "threshold":'BLOCK_NONE'},
                            {"category":'HARM_CATEGORY_HATE_SPEECH',
                             "threshold":'BLOCK_NONE'}
    ])
    chat = model.start_chat(history=[])
    response=chat.send_message(system_instruction)
    response=chat.send_message(message,generation_config=genai.types.GenerationConfig(candidate_count=1,
                                                                                        temperature=0))
    return response.text
