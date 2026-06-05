def create_html_table(df):

    html = """
    <table border="1"
           cellpadding="6"
           cellspacing="0"
           style="border-collapse: collapse;
                  font-family: Arial;
                  font-size: 13px;">

    <tr style="background-color:#f2f2f2;">
        <th>Stock</th>
        <th>Qty</th>
        <th>Avg Price</th>
        <th>LTP</th>
        <th>Current Value</th>
        <th>Today's Gain</th>
        <th>Total Gain</th>
        <th>Contribution %</th>
    </tr>
    """

    for _, row in df.iterrows():

        day_color = (
            "green"
            if row["Today's Gain"] >= 0
            else "red"
        )

        total_color = (
            "green"
            if row["Total Gain"] >= 0
            else "red"
        )

        html += f"""
        <tr>
            <td>{row['Stock']}</td>
            <td>{row['Qty']}</td>
            <td>₹{row['Avg Price']:,.2f}</td>
            <td>₹{row['LTP']:,.2f}</td>
            <td>₹{row['Current Value']:,.2f}</td>

            <td style="color:{day_color};
                       font-weight:bold;">
                ₹{row["Today's Gain"]:,.2f}
            </td>

            <td style="color:{total_color};
                       font-weight:bold;">
                ₹{row["Total Gain"]:,.2f}
            </td>

            <td>{row['Contribution %']}%</td>
        </tr>
        """

    html += "</table>"

    return html

def build_email_html(
    report_df,
    value,
    day_gain,
    total_gain,
    top_gainer,
    top_loser
):
    table_html = create_html_table(report_df)

    summary = f"""
    <div style="
        font-family: Segoe UI, Arial, sans-serif;
        font-size:16px;
        line-height:1.8;
        padding:15px;
        border:1px solid #ddd;
        border-radius:8px;
        background-color:#f8f9fa;
    ">

    <h2>📊 Daily Portfolio Summary</h2>

    <b>Portfolio Value:</b>
    ₹{value:,.2f}
    <br>

    <b>Today's Gain:</b>
    <span style="color:{'green' if day_gain >= 0 else 'red'};">
    ₹{day_gain:,.2f}
    </span>
    <br>

    <b>Total Gain:</b>
    <span style="color:{'green' if total_gain >= 0 else 'red'};">
    ₹{total_gain:,.2f}
    </span>
    <br><br>

    <b>🏆 Top Gainer:</b>
    {top_gainer['Stock']}
    (
    <span style="color:green;">
    ₹{top_gainer["Today's Gain"]:.2f}
    </span>
    )

    <br>

    <b>📉 Top Loser:</b>
    {top_loser['Stock']}
    (
    <span style="color:red;">
    ₹{top_loser["Today's Gain"]:.2f}
    </span>
    )

    </div>
    """

    return f"""
    <html>
    <body>

    {summary}

    <br><br>

    {table_html}

    </body>
    </html>
    """

