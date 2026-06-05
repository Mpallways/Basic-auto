import smtplib

from email.mime.text import (
    MIMEText
)

from email.mime.multipart import (
    MIMEMultipart
)

import os


def send_email(html):

    sender = os.getenv(
        "EMAIL_FROM"
    )

    receiver = os.getenv(
        "EMAIL_TO"
    )

    password = os.getenv(
        "EMAIL_PASSWORD"
    )

    msg = MIMEMultipart()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = (
        "Daily Portfolio Report"
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