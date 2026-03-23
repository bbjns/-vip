import os
from telegram.ext import Updater, CommandHandler

TG_TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = str(os.getenv("CHAT_ID"))

def check_user(update):
    return str(update.message.chat_id) == CHAT_ID

def start(update, context):
    if not check_user(update):
        update.message.reply_text("无权限")
        return
    update.message.reply_text("机器人测试成功")

updater = Updater(TG_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

print("Bot started")
updater.start_polling()
updater.idle()