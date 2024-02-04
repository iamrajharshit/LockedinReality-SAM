import chainlit as cl
import google.generativeai as genai
API_KEY = "AIzaSyAezKZT5ODtVc6bczVqg2FWQZ2YSIerbbY"

@cl.on_chat_start
def on_chat_start():
    print("A new chat session has started!")

@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here..

    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(message.content)

    await cl.Message(
        content=response.text
    ).send()

    



