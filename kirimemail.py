from email.message import EmailMessage
from getpass import getpass
from smtplib import SMTP_SSL
from sys import exit

print ("Selamat Datang")

while True:
    username = input("masukan email:")
    password = inputgetpass("masukan password:")
    sender =  input("masukan pengirim:")
    subject = input("masukan subjek:")
    content = input("masukan isi email:")





smtp_server = 'smtp.gmail.com'



# Create a text/plain message
msg = EmailMessage()
msg.set_content(content)

msg['Subject'] = subject
msg['From'] = sender
msg['To'] = destination

try:
    s = SMTP_SSL(smtp_server)
    s.login(username, password)
    try:
        s.send_message(msg)
    finally:
        s.quit()

except Exception as E:
    exit('Mail failed: {}'.format(str(E)))

