import os

from auth import get_client
from portfolio import fetch_holdings
from portfolio_metrics import calculate_metrics
from report_html import build_email_html
import pandas as pd

client = get_client()
df = fetch_holdings(client)

results, value, day_gain, total_gain = calculate_metrics(
    df,
    client
)
report_df = pd.DataFrame(results)

report_df = report_df.sort_values(
    by="Today's Gain",
    ascending=False
)
report_df["Contribution %"] = (
    report_df["Current Value"] /
    report_df["Current Value"].sum()
    * 100
).round(2)

top_gainer = report_df.iloc[0]

top_loser = report_df.iloc[-1]



print(report_df)

print(f"Portfolio Value: ₹{value:,.2f}")
print(f"Today's Gain: ₹{day_gain:,.2f}")
print(f"Total Gain: ₹{total_gain:,.2f}")

from report import (
    generate_summary
)

from email_sender import (
    send_email
)


os.makedirs(
    "data",
    exist_ok=True
)

df.to_csv(
    "data/holdings.csv",
    index=False
)

html = build_email_html(
    report_df,
    value,
    day_gain,
    total_gain,
    top_gainer,
    top_loser
)

send_email(html)

print(
    "Portfolio Report Sent"
)