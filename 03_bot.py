import os
import re
import time

import pyautogui
import pyperclip
from openai import OpenAI

# ---------------- CONFIG (edit for your own screen and chat) ----------------
MY_NAME = "Naruto"            # your name as it appears in the chat
FRIEND_NAME = "Friend Name"   # the person the bot should reply to
MODEL = "gpt-3.5-turbo"

# Screen positions: find yours by running 01_get_cursor.py
BROWSER_ICON = (1639, 1412)       # taskbar icon of the browser with the chat open
CHAT_START = (972, 202)           # top-left corner of the chat area
CHAT_END = (2213, 1278)           # bottom-right corner of the chat area
DESELECT_CLICK = (1994, 281)      # empty spot to clear the text selection
MESSAGE_BOX = (1808, 1328)        # the "type a message" box

CHECK_INTERVAL = 5                # seconds between each check
# -----------------------------------------------------------------------------

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Matches lines like: [20:30, 12/6/2024] Name: message
HEADER = re.compile(r"^\[\d{1,2}:\d{2}, \d{1,2}/\d{1,2}/\d{4}\] ([^:]+):")


def last_sender(chat_log):
    """Return the name of whoever sent the last message in the copied chat."""
    sender = None
    for line in chat_log.splitlines():
        match = HEADER.match(line.strip())
        if match:
            sender = match.group(1).strip()
    return sender


def generate_reply(chat_history):
    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": f"You are a person named {MY_NAME} who speaks Hindi as well as English. You are from India and you are a coder. You analyze chat history and reply in a funny, friendly way. Output should be the next chat response (text message only).",
            },
            {
                "role": "system",
                "content": "Do not start your reply with a timestamp or a name like [21:02, 12/6/2024] Name:",
            },
            {"role": "user", "content": chat_history},
        ],
    )
    return completion.choices[0].message.content


def main():
    # Move the mouse to a screen corner to stop the bot instantly (pyautogui failsafe)
    pyautogui.click(*BROWSER_ICON)
    time.sleep(1)

    while True:
        time.sleep(CHECK_INTERVAL)

        # Select and copy the visible chat
        pyautogui.moveTo(*CHAT_START)
        pyautogui.dragTo(*CHAT_END, duration=2.0, button="left")
        pyautogui.hotkey("ctrl", "c")
        time.sleep(2)
        pyautogui.click(*DESELECT_CLICK)

        chat_history = pyperclip.paste()
        print(chat_history)

        if last_sender(chat_history) == FRIEND_NAME:
            reply = generate_reply(chat_history)
            pyperclip.copy(reply)

            pyautogui.click(*MESSAGE_BOX)
            time.sleep(1)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(1)
            pyautogui.press("enter")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Bot stopped.")
