from asyncio.base_events import Server
import smtplib

sender_email = "nabegh.muhra35@gmail.com"
rec_email = "muhrafamily@gmail.com"
password = input(str("password? : "))
message = "Hey, this was sent to you by python"

sever = smtplib.SMTP('smtp.gmail.com', 587)
Server.starttls()
Server.login(sender_email, password)
print("login success")
Server.sendmail(sender_email, rec_email, message)
print("Email has been sent to", rec_email)
