from email.message import EmailMessage
from getpass import getpass
from smtplib import SMTP_SSL
from sys import exit


print ("Selamat Datang")

username = input("masukan email:")
password = input(getpass("masukan password:"))
n=int(input("Masukkan jumlah penerima : "))
f=open("receiver_list.txt","w")

daftar_email=[]
for x in range(n):
    sender=input("Masukkan email penerima  : ")
    daftar_email.append(sender)
    f.write(sender+'\n')
f.close()

subject = input("masukan subjek:")
content = input("masukan isi email:")




    
smtp_server = 'smtp.gmail.com'
# Create a text/plain message
msg = EmailMessage()
msg.set_content(content)

msg['Subject'] = subject
msg['From'] = sender
msg['To'] = destination

try: # baris program yang kemungkinan akan terjadi error  diserahkan kepada blok except
    s = SMTP_SSL(smtp_server)
    s.login(username, password)
    try:
        s.send_message(msg)
    finally:
        s.quit()

except Exception as E:
    exit('Mail failed: {}'.format(str(E)))

