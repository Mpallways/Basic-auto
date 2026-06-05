def generate_summary(df):

    total_stocks = len(df)

    summary = f"""
Portfolio Summary

Total Holdings : {total_stocks}
"""

    return summary