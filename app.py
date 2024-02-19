import chainlit as cl
from src.llm import ask_order, history

@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here..
    #history.append({"role": "user", "text": message.content})
    response=ask_order(message.content)
    #history.append({"role": "model", "text": response})
    await cl.Message(
        content=response
    ).send()

    



