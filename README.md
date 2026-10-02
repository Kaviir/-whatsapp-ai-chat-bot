# AI Chat Auto-Reply Bot

A Python automation bot that reads a chat on screen (WhatsApp Web format), generates a reply with the OpenAI API, and types it back automatically.

## How it works
1. Selects and copies the visible chat using screen automation (`pyautogui`).
2. Reads the copied text from the clipboard (`pyperclip`).
3. Checks who sent the last message.
4. If it was your friend, sends the chat history to OpenAI and gets a reply.
5. Pastes the reply into the message box and presses Enter.

## Files
| File | Purpose |
|------|---------|
| `01_get_cursor.py` | Prints your mouse position so you can find screen coordinates |
| `02_openai.py` | Tests the OpenAI reply generation on a sample chat |
| `03_bot.py` | The main auto-reply bot |

## Tech Stack
Python, PyAutoGUI, Pyperclip, OpenAI API

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Kaviir/whatsapp-ai-chat-bot.git
   cd whatsapp-ai-chat-bot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key (Windows CMD), then restart the terminal:
   ```
   setx OPENAI_API_KEY "your_openai_key"
   ```
4. Run `python 01_get_cursor.py` and note the screen coordinates of the chat area and the message box.
5. Open `03_bot.py` and update the CONFIG section (`MY_NAME`, `FRIEND_NAME` and the coordinates).
6. Open the chat in your browser and run:
   ```bash
   python 03_bot.py
   ```

To stop the bot, press `Ctrl+C` in the terminal or move the mouse to a screen corner.

## Disclaimer
Built for learning and personal experiments. Use it only in chats where the other person knows about it, and follow the terms of the messaging platform you use.

## Future Improvements
- Auto-detect screen positions instead of fixed coordinates
- Add reply tone options (funny, formal, friendly)
- Use the official messaging APIs instead of screen automation
