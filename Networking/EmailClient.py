import smtplib
from email.mime.text import MIMEText

body = "How are you?"

msg = MIMEText(body)

msg["From"] = "xxxx@gmail.com"
msg["To"] = "xxxx123@gmail.com"
msg["Subject"] = "Hello"

server = smtplib.SMTP("smtp.gmail.com",587)

server.starttls()

server.login("xxxx@gmail.com","password")

server.send_message(msg)

print("Mail Sent.")

server.quit()