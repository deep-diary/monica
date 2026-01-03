import smtplib

sender = "Private Person <hello@deep-diary.com>"
receiver = "A Test User <deep-diary@qq.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
    server.starttls()
    server.login("smtp@mailtrap.io", "94eb5c74b8a5d7b2c57104ce7ab53d88")
    server.sendmail(sender, receiver, message)
