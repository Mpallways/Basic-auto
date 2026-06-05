import smtplib

from email.mime.text import (
    MIMEText
)

from email.mime.multipart import (
    MIMEMultipart
)

import os


def send_email(
        html,
        value,
        day_gain
    ):

    sender = os.getenv("EMAIL_FROM")

    receiver = os.getenv("EMAIL_TO")

    password = os.getenv("EMAIL_PASSWORD")

    msg = MIMEMultipart()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = (
        f"📈 Portfolio ₹{value:,.0f} | "
        f"Day Gain ₹{day_gain:,.0f}"
    )

    msg.attach(
        MIMEText(
            html,
            "html"
        )
    )

    server = smtplib.SMTP(
        "smtp.gmail.com",
        587
    )

    server.starttls()

    server.login(
        sender,
        password
    )

    server.send_message(
        msg
    )

    server.quit()
