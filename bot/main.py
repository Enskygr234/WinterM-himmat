"""Botun giriş noktası: python -m bot.main"""
import logging
import os

from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from bot import handlers

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)


def build_app(token: str) -> Application:
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", handlers.start))
    app.add_handler(CommandHandler("help", handlers.help_command))
    app.add_handler(CommandHandler("hakkinda", handlers.hakkinda))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.echo))
    return app


def main() -> None:
    load_dotenv()
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise SystemExit("BOT_TOKEN bulunamadı. .env.example dosyasını .env olarak kopyalayıp token'ı yaz.")
    build_app(token).run_polling()


if __name__ == "__main__":
    main()
