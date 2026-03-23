import os
import ccxt
from telegram.ext import Updater, CommandHandler
TG_TOKEN = os.getenv(jsc6bot)
CHAT_ID = str(os.getenv(qy2200)
API_KEY = os.getenv(bg_7d494ac9f8b27e9b682f41bc3126ff73)
API_SECRET = os.getenv(77a3bba9fcb9b0dea28bcadf8ae9e5d6500f881b3612e160735365d5fcdf3abb)
API_PASSWORD = os.getenv(577779188)
exchange = ccxt.bitget({
'apiKey': API_KEY,
'secret': API_SECRET,
'password': API_PASSWORD,
'enableRateLimit': True,
'options': {'defaultType': 'swap'}
})
def check_user(update):
return str(update.message.chat_id) == CHAT_ID
def start(update, context):
    if not check_user(update):
        update.message.reply_text("无权限")
        return
    update.message.reply_text("机器人已启动")

def balance(update, context):
    if not check_user(update):
        update.message.reply_text("无权限")
        return
    balance = exchange.fetch_balance()
    usdt = balance['USDT']['free']
    update.message.reply_text("USDT余额: " + str(usdt))

def long(update, context):
    if not check_user(update):
        update.message.reply_text("无权限")
        return
    symbol = "BTC/USDT:USDT"
    amount = 0.001
    exchange.create_market_buy_order(symbol, amount)
    update.message.reply_text("已开多")

def short(update, context):
    if not check_user(update):
        update.message.reply_text("无权限")
        return
    symbol = "BTC/USDT:USDT"
    amount = 0.001
    exchange.create_market_sell_order(symbol, amount)
    update.message.reply_text("已开空")

updater = Updater(TG_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("balance", balance))
dp.add_handler(CommandHandler("long", long))
dp.add_handler(CommandHandler("short", short))

updater.start_polling()
updater.idle()