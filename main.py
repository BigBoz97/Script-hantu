import json
import asyncio
from telethon import TelegramClient

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

if __name__ == "__main__":
    asyncio.run(main())
