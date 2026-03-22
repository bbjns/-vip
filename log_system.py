import csv
import os
from datetime import datetime

file_name = "trades.csv"

if not os.path.exists(file_name):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["时间","币种","方向","入场价","出场价","止损","止盈","盈亏","手续费","余额"])

def log_trade(symbol, side, entry, exit_price, sl, tp, pnl, fee, balance):
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), symbol, side, entry, exit_price, sl, tp, pnl, fee, balance])
