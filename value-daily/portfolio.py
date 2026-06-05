import pandas as pd
def fetch_holdings(client):
    response = client.get_holdings_for_user()
    holdings = response["holdings"]
    df = pd.DataFrame(holdings)
    return df