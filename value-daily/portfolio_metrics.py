import pandas as pd
import yfinance as yf

def calculate_metrics(df, client):

    results = []

    portfolio_value = 0
    portfolio_day_gain = 0
    portfolio_total_gain = 0

    for _, row in df.iterrows():

        symbol = row["trading_symbol"]

        qty = row["quantity"]

        avg_price = row["average_price"]

        try:

            ticker = yf.Ticker(f"{symbol}.NS")

            hist = ticker.history(period="2d")

            if len(hist) < 2:
                print(f"Not enough data for {symbol}")
                continue

            ltp = hist["Close"].iloc[-1]

            prev_close = hist["Close"].iloc[-2]

            day_change = ltp - prev_close

            current_value = qty * ltp

            day_gain = qty * day_change

            total_gain = qty * (
                ltp - avg_price
            )

            portfolio_value += current_value

            portfolio_day_gain += day_gain

            portfolio_total_gain += total_gain

            results.append({
                "Stock": symbol,
                "Qty": qty,
                "Avg Price": round(avg_price,2),
                "LTP": round(ltp,2),
                "Current Value": round(current_value,2),
                "Today's Gain": round(day_gain,2),
                "Total Gain": round(total_gain,2)
            })

        except Exception as ex:

            print(
                f"Failed {symbol}: {ex}"
            )

    return (
        results,
        portfolio_value,
        portfolio_day_gain,
        portfolio_total_gain
    )