"""Komut ve mesaj işleyicileri."""
from telegram import Update
from telegram.ext import ContextTypes

YARDIM_METNI = (
    "Kullanabileceğin komutlar:\n"
    "/start - Botu başlat\n"
    "/help - Bu yardım mesajını göster\n"
    "/hakkinda - Bot hakkında bilgi\n\n"
    "Komut olmayan her mesajı sana geri yazarım."
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ad = update.effective_user.first_name if update.effective_user else "dostum"
    await update.message.reply_text(
        f"Merhaba {ad}! 👋 Ben WinterM botuyum.\n/help yazarak neler yapabildiğimi görebilirsin."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(YARDIM_METNI)


async def hakkinda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("WinterM-himmat Telegram botu • python-telegram-bot ile yazıldı.")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)
