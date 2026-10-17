# WinterM-himmat

Python ile yazılmış Telegram botu ([python-telegram-bot](https://python-telegram-bot.org/)).

## Kurulum

1. Telegram'da [@BotFather](https://t.me/BotFather)'a `/newbot` yaz, bota isim ver ve **token**'ı al.
2. Bağımlılıkları kur:
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. `.env.example` dosyasını `.env` olarak kopyala ve `BOT_TOKEN` değerini yaz.
4. Botu çalıştır:
   ```bash
   python -m bot.main
   ```

## Komutlar

| Komut | Açıklama |
|---|---|
| `/start` | Karşılama mesajı |
| `/help` | Komut listesi |
| `/hakkinda` | Bot hakkında bilgi |
| (düz metin) | Mesajı geri yazar (echo) |

## Yeni komut eklemek

`bot/handlers.py` içine bir `async def` fonksiyon yaz, sonra `bot/main.py` içindeki `build_app` fonksiyonunda `CommandHandler("komut", handlers.fonksiyon)` olarak kaydet.
