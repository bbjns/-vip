import telebot
import threading
import time
from config import TG_TOKEN, CHAT_ID
from strategy import run_strategy
from stats import get_stats
from equity import max_drawdown

bot = telebot.TeleBot(TG_TOKEN)
running = False

def menu():
    from telebot.types import ReplyKeyboardMarkup
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("启动交易", "停止交易")
    markup.row("交易统计", "最大回撤")
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(CHAT_ID, "量化交易系统已连接", reply_markup=menu())

@bot.message_handler(func=lambda message: True)
def control(message):
    global running

    if message.text == "启动交易":
        running = True
        bot.send_message(CHAT_ID, "交易系统启动")

    elif message.text == "停止交易":
        running = False
        bot.send_message(CHAT_ID, "交易系统停止")

    elif message.text == "交易统计":
        s = get_stats()
        bot.send_message(CHAT_ID, str(s))

    elif message.text == "最大回撤":
        dd = max_drawdown()
        bot.send_message(CHAT_ID, f"最大回撤: {dd}%")

def trading_loop():
    while True:
        if running:
            run_strategy()
        time.sleep(5)

threading.Thread(target=trading_loop).start()
bot.polling()
