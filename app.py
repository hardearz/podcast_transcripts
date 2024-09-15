import os
from dotenv import load_dotenv

import chainlit as cl
from chainlit.types import ThreadDict
from chainlit.input_widget import Tags
from chainlit.input_widget import Select

import utils


@cl.on_chat_start
async def on_chat_start():
    load_dotenv()  # take environment variables


@cl.on_message
async def main(message: cl.Message):


    chat_id = cl.user_session.get("chat_id")
    print("CHAT ID:", chat_id)
    if chat_id:
        response = utils.chat_vectara(message.content, chat_id)
    else:
        response = utils.create_chat_vectara(message.content)
        cl.user_session.set("chat_id", response["chat_id"])

    await cl.Message(
        content=(
            response["answer"]
            # + "\n" +
            # "\n".join(
            #     r["text"] + "\n" + r["document_metadata"]["title"] + " " +
            #     (r["part_metadata"]["timestamp"] if "timestamp" in r["part_metadata"] else "")
            #     for r in response["search_results"]
            # )
        )
    ).send()
    

@cl.on_stop
def on_stop():
    pass


@cl.on_chat_end
def on_chat_end():
    cl.user_session.set("chat_id", None)
    pass
    

@cl.on_chat_resume
async def on_chat_resume(thread: ThreadDict):
    pass


# @cl.set_starters
# async def set_starters():
#     return [
#         cl.Starter(
#             label="Morning routine ideation",
#             message="Can you help me create a personalized morning routine that would help increase my productivity throughout the day? Start by asking me about my current habits and what activities energize me in the morning.",
#             #icon="/public/idea.svg",
#             ),

#         cl.Starter(
#             label="Explain superconductors",
#             message="Explain superconductors like I'm five years old.",
#             #icon="/public/learn.svg",
#             ),
#         cl.Starter(
#             label="Python script for daily email reports",
#             message="Write a script to automate sending daily email reports in Python, and walk me through how I would set it up.",
#             #icon="/public/terminal.svg",
#             ),
#         cl.Starter(
#             label="Text inviting friend to wedding",
#             message="Write a text asking a friend to be my plus-one at a wedding next month. I want to keep it super short and casual, and offer an out.",
#             #icon="/public/write.svg",
#             )
#         ]

# @cl.set_chat_profiles
# async def chat_profile(current_user: cl.User):
#     if current_user.metadata["role"] != "ADMIN":
#         return None

#     return [
#         cl.ChatProfile(
#             name="My Chat Profile",
#             icon="https://picsum.photos/250",
#             markdown_description="The underlying LLM model is **GPT-3.5**, a *175B parameter model* trained on 410GB of text data.",
#             starters=[
#                 cl.Starter(
#                     label="Morning routine ideation",
#                     message="Can you help me create a personalized morning routine that would help increase my productivity throughout the day? Start by asking me about my current habits and what activities energize me in the morning.",
#                     #icon="/public/idea.svg",
#                 ),
#                 cl.Starter(
#                     label="Explain superconductors",
#                     message="Explain superconductors like I'm five years old.",
#                     #icon="/public/learn.svg",
#                 ),
#             ],
#         )
#     ]