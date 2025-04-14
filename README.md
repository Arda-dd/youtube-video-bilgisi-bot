# YouTube Video Bilgisi Çekici Bot 🚀

Bu Python botu, **YouTube** video linklerini vererek, **video başlığı**, **açıklama**, **izlenme sayısı**, **yayın tarihi** gibi bilgileri **Telegram** üzerinden almanızı sağlar.

---

## 🧰 Kullanılan Teknolojiler

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) – YouTube video bilgilerini çekmek için
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) – Telegram botu ile mesajlaşmak için

---

## ⚙️ Kurulum

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/kullanici_adin/repo_adi.git
   cd repo_adi

Gerekli paketleri kurun:
pip install -r requirements.txt

config.py dosyasını oluşturun ve içine bot token’ınızı ve chat ID’nizi ekleyin:
TELEGRAM_TOKEN = "bot-token-buraya"
CHAT_ID = "chat-id-buraya"

Video linklerini eklemek için links.txt dosyasına her satıra bir YouTube linki ekleyin

🚀 Çalıştırmak için
python youtube.py

Yapımcı: Arda Tınmazoğlu