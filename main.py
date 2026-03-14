import json
import asyncio
from telethon import TelegramClient, events

def banner():
    print("=================================")
    print(" ClickBee LTC Bot Skeleton ")
    print("=================================")

async def main():

    banner()

    config = json.load(open("config.json"))

    api_id = config["api_id"]
    api_hash = config["api_hash"]
    bot_username = config["bot_username"]

    client = TelegramClient("session/session", api_id, api_hash)

    await client.start()

    print("Login success")

    await client.send_message(bot_username, "/start")

    print(f"Connected to @{bot_username}")
    @client.on(events.NewMessage(from_users=bot_username))
async def handler(event):
    print("\n===== BOT MESSAGE =====")
    print(event.raw_text)

print("Listening for messages from bot...")
await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
