import pandas as pd

def get_stats():
    df = pd.read_csv("trades.csv")
    total = len(df)
    win = len(df[df["盈亏"] > 0])
    pnl = df["盈亏"].sum()

    return {
        "交易次数": total,
        "胜率": round(win / total * 100, 2) if total > 0 else 0,
        "总收益": round(pnl, 2)
    }
