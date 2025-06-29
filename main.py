from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import random

ADMIN_ID = 1011796703
YUSUF_ID = 1556883581
APO_ID = 1586947929

apo_receives = [
    "SUS LAN NUMAN",
    "SUS LAN ŞİŞKO",
]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id == YUSUF_ID:
        await update.message.reply_text("YARRRMA YUSUF")
    elif update.message.from_user.id == APO_ID:
        if update.message.text in apo_receives:
            await update.message.reply_text(random.choice(apo_receives))

app = ApplicationBuilder().token("8135407514:AAEGKIjMHWsPUaG4_a9sGrFneOEtsR4Y4qc").build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
