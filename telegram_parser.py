from telethon.sync import TelegramClient
from config import API_ID, API_HASH, CHANNEL

def get_jokes(limit=10):
    jokes = []
    with TelegramClient('anon', API_ID, API_HASH) as client:
        for message in client.iter_messages(CHANNEL, limit=limit):
            if message.message:
                jokes.append({
                    'id': message.id,
                    'text': message.message,
                    'date': str(message.date)
                })
    return jokes
