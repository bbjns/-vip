from exchange import get_price, open_long
from risk import calc_position
from log_system import log_trade
from config import SYMBOL, TAKE_PROFIT, STOP_LOSS

last_price = 0

def run_strategy():
    global last_price

    price = get_price(SYMBOL)

    if last_price == 0:
        last_price = price
        return

    if price > last_price * 1.003:
        qty = calc_position(price)
        entry = price
        sl = entry * (1 - STOP_LOSS)
        tp = entry * (1 + TAKE_PROFIT)

        open_long(SYMBOL, qty)

        exit_price = get_price(SYMBOL)
        pnl = (exit_price - entry) * qty

        log_trade(SYMBOL, "LONG", entry, exit_price, sl, tp, pnl, 0, 0)

    last_price = price
