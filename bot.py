"""
Solurix Welcome Bot
--------------------
Jab bhi koi naya member group me join kare, bot use ek welcome
message bhejega. Simple aur customizable.

Setup:
1. pip install -r requirements.txt
2. .env file me apna BOT_TOKEN daalo (BotFather se lo)
3. python bot.py chalao
4. Bot ko apne group me add karo aur ADMIN bana do
   (admin banana zaroori hai warna ye naye members detect
   nahi kar payega kuch group settings me)
"""

import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    ChatMemberHandler,
    ContextTypes,
)

# ---------- Setup ----------
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ---------- Customize your welcome message here ----------
WELCOME_TEMPLATE = (
    "👋 Namaste {mention}!\n\n"
    "*{group_name}* me tumhara swagat hai! 🎉\n\n"
    "Kuch rules follow karo:\n"
    "• Respectful raho 🙏\n"
    "• Spam/promotion allowed nahi hai 🚫\n"
    "• Enjoy karo aur naye dost banao! 🤝\n"
)


async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Jab koi member group join kare to ye function trigger hota hai."""
    result = update.chat_member
    if result is None:
        return

    old_status = result.old_chat_member.status
    new_status = result.new_chat_member.status

    # Sirf tab trigger ho jab member "left/kicked" se "member" bana ho
    # (yani naya join, purane member ka status-change nahi)
    joined_now = old_status in ("left", "kicked") and new_status == "member"
    if not joined_now:
        return

    user = result.new_chat_member.user
    chat = result.chat

    mention = f"[{user.full_name}](tg://user?id={user.id})"
    text = WELCOME_TEMPLATE.format(mention=mention, group_name=chat.title)

    await context.bot.send_message(
        chat_id=chat.id,
        text=text,
        parse_mode=ParseMode.MARKDOWN,
    )
    logger.info(f"Welcomed {user.full_name} in {chat.title}")


def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN .env file me set nahi hai!")

    app = Application.builder().token(BOT_TOKEN).build()

    # chat_member updates ke liye handler (naye join ko catch karta hai)
    app.add_handler(ChatMemberHandler(welcome_new_member, ChatMemberHandler.CHAT_MEMBER))

    logger.info("Solurix Welcome Bot start ho gaya...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
