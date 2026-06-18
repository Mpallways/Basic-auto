import gspread
from google.oauth2.service_account import Credentials

def fetch_holdings():

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    
    creds = Credentials.from_service_account_file(
        "portfoliotracker-june-2927b58e2103.json",
        scopes=scopes
    )

    print("Service Account:")
    print(creds.service_account_email)

    client = gspread.authorize(creds)

    print("Authentication successful")

    sheet = client.open_by_key(
        "1jUe2hJwaFAbVMycy6Rgpa2FLs0ZMZaPR2klXnLAHkMQ"
    ).sheet1

    records = sheet.get_all_records()

    print("\nGOOGLE SHEET RECORDS\n")
    print(records)

    return records
