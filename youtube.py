import yt_dlp
from datetime import datetime
import asyncio
from telegram import Bot
from config import TELEGRAM_TOKEN, CHAT_ID

async def send_telegram_message(message):
    bot = Bot(token=TELEGRAM_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message)

def video_bilgisi_cek(url):
    ydl_opts = {}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        raw_date = info.get('upload_date')
        try:
            upload_date = datetime.strptime(raw_date, "%Y%m%d").strftime("%d %B %Y")
        except:
            upload_date = "Tarih alınamadı"

        message = f"""
🎥 Başlık: {info.get('title')}
📺 Kanal: {info.get('uploader')}
👁️ İzlenme: {info.get('view_count')}
🗓️ Yayın Tarihi: {upload_date}
📝 Açıklama: {info.get('description')[:300]}...
"""
        asyncio.run(send_telegram_message(message))

def toplu_video_bilgisi_cek(dosya_adi):
    with open(dosya_adi, "r", encoding="utf-8") as file:
        links = file.readlines()
        for link in links:
            link = link.strip()
            if link:
                print(f"🎯 Video bilgisi çekiliyor: {link}")
                video_bilgisi_cek(link)

if __name__ == "__main__":
    toplu_video_bilgisi_cek("links.txt")
