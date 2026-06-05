import smtplib
from datetime import datetime
from zoneinfo import ZoneInfo
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
    current_time = (
        datetime.now(
        ZoneInfo("Asia/Kolkata")
        )
        .strftime("%d-%b-%Y %I:%M %p IST")
    )
    hour = datetime.now(
        ZoneInfo("Asia/Kolkata")
    ).hour
    
    if hour < 15:
        run_name = "🕛 Noon Portfolio Report"
    else:
        run_name = "🔔 Market Close Report"
        
    msg["Subject"] = (
        f"{run_name} | "
        f"{current_time}"
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
