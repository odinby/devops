import pandas as pd
import smtplib

SenderAddress = "odinsmail@gmail.com"
password = "lmurehvtrfxndyeg"

e = pd.read_excel("email.xlsx")
emails = e['Emails'].values

server = smtplib.SMTP("smtp.gmail.com, 587")
server.starttls()
server.login(SenderAddress, password)

msg = "Test messages from python"
subject = "TEST email"

body = "Subject: {}\n\n{}".format(subject.msg)

for email in emails:
    server.sendmail(SenderAddress, email, body)

server.quit()
