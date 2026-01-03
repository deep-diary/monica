import mailtrap as mt

mail = mt.Mail(
    sender=mt.Address(email="hello@deep-diary.com", name="Mailtrap Test"),
    to=[mt.Address(email="deep-diary@qq.com")],
    subject="You are awesome!",
    text="Congrats for sending test email with Mailtrap!",
    category="Integration Test",
)

client = mt.MailtrapClient(token="94eb5c74b8a5d7b2c57104ce7ab53d88")
response = client.send(mail)

print(response)