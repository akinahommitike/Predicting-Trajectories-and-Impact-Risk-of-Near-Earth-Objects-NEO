import chainlit as cl

#continous on a loop

@cl.on_message
def main(message:str):
    #Your string goes here
    result=message.title()

    #send a response back to user
    cl.send_message(content=f"Sure,here is a message:{result}")