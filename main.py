import json
import asyncio
import random # Untuk jeda acak
from telethon import TelegramClient, events

def banner():
    print("=" * 45)
    print("   CLICKBEE AUTO-BOT [ANTI-BAN ENABLED]   ")
    print("=" * 45)

async def main():
    banner()

    try:
        with open("config.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        print("[-] Error: config.json hilang!")
        return

    # Sesi unik agar tidak bentrok
    client = TelegramClient("session_ana", config["api_id"], config["api_hash"])
    
    await client.start()
    print("[+] Login Berhasil! Menunggu instruksi...")

    bot_user = config["bot_username"]
    await client.send_message(bot_user, "/start")

    @client.on(events.NewMessage(from_users=bot_user))
    async def handler(event):
        message_text = event.raw_text
        
        # Simulasi 'Sedang Mengetik' atau 'Membaca'
        async with client.action(bot_user, 'typing'):
            # Jeda acak antara 3 - 7 detik sebelum merespons pesan
            delay = random.uniform(3.5, 7.2)
            print(f"[*] Menunggu {delay:.2f} detik (Anti-Spam)...")
            await asyncio.sleep(delay)

        if event.reply_markup:
            for row in event.reply_markup.rows:
                for button in row.buttons:
                    # Filter tombol yang umum digunakan untuk earning
                    target_buttons = ["Visit", "View", "Go to", "Open link"]
                    
                    if any(target in button.text for target in target_buttons):
                        print(f"[#] Mencoba klik: {button.text}")
                        try:
                            # Klik tombol
                            await event.click(button)
                            
                            # Jeda panjang setelah klik sukses (simulasi melihat iklan)
                            wait_after_click = random.randint(15, 30)
                            print(f"[+] Berhasil! Menunggu {wait_after_click} detik sebelum aksi berikutnya...")
                            await asyncio.sleep(wait_after_click)
                            
                        except Exception as e:
                            print(f"[!] Gagal klik: {e}")
        
        # Jika bot mengirim pesan "No more tasks", kita istirahat lebih lama
        if "no more tasks" in message_text.lower():
            print("[!] Tugas habis. Istirahat 10 menit untuk menghindari deteksi...")
            await asyncio.sleep(600) 
            await client.send_message(bot_user, "/start")

    print("[*] Bot berjalan dengan mode senyap...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[!] Dimatikan secara manual.")
