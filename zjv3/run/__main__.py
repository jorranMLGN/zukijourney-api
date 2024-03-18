import chainlit as cl
from openai import OpenAI


client = OpenAI(
    # This is the default and can be omitted
    api_key="zu-6e6c20a8ce684183ca133da4914c5c74",
    base_url="https://zukijourney.xyzbot.net/v1"  # or "https://zukijourney.xyzbot.net/unf"

)


@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    chat_completion = client.chat.completions.create(
        stream=True,  # can be true
        model="gpt-4",  # or "gpt-3.5"
        messages=[
            {
                "role": "user",
                "content": f'{message}',  # responds 2: gpt-4, responds 1: gpt-3.5
            },
        ],
    )
    # Send a response back to the user
    await cl.Message(
        content=f"Received: {chat_completion.choices[0].delta.content}",
    ).send()

#
# chat_completion = client.chat.completions.create(
#     stream=True, # can be true
#     model="gpt-4", # or "gpt-3.5"
#     messages=[
#         {
#             "role": "user",
#             "content": 'what is the difference between a dog and a cat?', #responds 2: gpt-4, responds 1: gpt-3.5
#         },
#     ],
# )
#
#
# for chunk in chat_completion:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")