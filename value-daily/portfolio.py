import pandas as pd
import json
import os
import gspread
from google.oauth2.service_account import Credentials


def fetch_holdings():

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    if os.path.exists("portfoliotracker-june-2927b58e2103.json"):
        creds = Credentials.from_service_account_file(
        "portfoliotracker-june-2927b58e2103.json",
        scopes=scopes
    )
    else:
        service_account_info = json.loads(
            os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"]
        )

        creds = Credentials.from_service_account_info(
            service_account_info,
            scopes=scopes
        )

    client = gspread.authorize(creds)

    sheet = client.open_by_key(
        "1jUe2hJwaFAbVMycy6Rgpa2FLs0ZMZaPR2klXnLAHkMQ"
    ).sheet1

    records = sheet.get_all_records()

    df = pd.DataFrame(records)

    df["Qty"] = (
        df["Qty"]
        .astype(str)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    df["Avg Price"] = (
        df["Avg Price"]
        .astype(str)
        .str.replace("₹", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    return df
