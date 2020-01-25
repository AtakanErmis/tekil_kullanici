import os
from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

async def main():
    users = set()
    async for dialog in client.iter_dialogs():
        if dialog.name.startswith('{ ek'):
            async for participant in client.iter_participants(dialog):
                users.add(participant.id)
                print(len(users), end="\r")
    print(len(users))

with TelegramClient('anon', api_id, api_hash) as client:
    client.loop.run_until_complete(main())
