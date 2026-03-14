import json
import asyncio
from telethon import TelegramClient, events

def banner():
    print("=" * 40)
    print("   CLICKBEE AUTOMATIC BOT - ACTIVE   ")
    print("=" * 40)

async def main():
    banner()

    # 1. Load Config
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        print("[-] Error: config.json tidak ditemukan!")
        return

    # 2. Inisialisasi Client
    # Menggunakan session di folder root agar lebih simpel
    client = TelegramClient("session_ana", config["api_id"], config["api_hash"])
    
    await client.start()
    print("[+] Login Berhasil!")

    bot_user = config["bot_username"]
    
    # 3. Kirim /start untuk memicu menu
    await client.send_message(bot_user, "/start")
    print(f"[+] Menghubungi {bot_user}...")

    # 4. Handler Pesan Otomatis
    @client.on(events.NewMessage(from_users=bot_user))
    async def handler(event):
        message_text = event.raw_text
        print(f"\n[Menerima Pesan]:\n{message_text}")

        # LOGIC: Jika ada tombol, coba klik tombol pertama (biasanya Visit/View)
        if event.reply_markup:
            for row in event.reply_markup.rows:
                for button in row.buttons:
                    # Kamu bisa memfilter berdasarkan teks tombol
                    if "Visit" in button.text or "View" in button.text:
                        print(f"[*] Mengklik tombol: {button.text}")
                        try:
                            # Menjalankan klik otomatis
                            await event.click(button)
                            # Beri jeda agar tidak terdeteksi spam/bot sangat cepat
                            await asyncio.sleep(2) 
                        except Exception as e:
                            print(f"[!] Gagal klik: {e}")

    print("[*] Bot sedang berjalan... Tekan Ctrl+C untuk berhenti.")
    await client.run_until_disconnected()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[!] Bot dihentikan oleh pengguna.")
