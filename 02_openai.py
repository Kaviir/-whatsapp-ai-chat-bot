import os

from openai import OpenAI

# Set the OPENAI_API_KEY environment variable before running
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Sample chat history (WhatsApp Web copy format)
chat_history = """
[20:30, 12/6/2024] Alex: Bro suggest something to listen while coding
[20:30, 12/6/2024] Sam: Try lo-fi beats
[20:31, 12/6/2024] Alex: Send me some English songs too
[20:31, 12/6/2024] Sam: Hold on
[20:32, 12/6/2024] Sam: This one is a Hindi-English mix but it's the best
[20:33, 12/6/2024] Alex: Okay okay
"""

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a person named Alex who speaks Hindi as well as English. You are from India and you are a coder. You analyze chat history and respond like Alex.",
        },
        {"role": "user", "content": chat_history},
    ],
)

print(completion.choices[0].message.content)
