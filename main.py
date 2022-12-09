import smtplib
import socket
from email.message import EmailMessage
from hidden import password, sender, reciever, reciever2
from time import sleep

# I know I misspelled reciever in my variables :/
email_address = sender
email_password = password

# changes array of emails to format that EmailMessage allows
reciever3 = ""
for i in range(0, len(reciever2)):
    if i == 0:
        reciever3 += reciever2[i]
    else:
        reciever3 += ", " + reciever2[i]
print("receiver 3 = " + reciever3)

# Constructs the email
msg = EmailMessage()
msg['Subject'] = "Aqua-phonics Garden Alert"
msg['From'] = email_address
msg['To'] = reciever3
msg.set_content("System has detected a leak and both motors have been shut off")

# Checks for internet then sends when it can, or else it will continuously check every 5 seconds
internet = False
while (internet != True):
    try:
        # send email
        with smtplib.SMTP_SSL('smtp-relay.sendinblue.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
        internet = True
    except socket.gaierror as err:
        print(err)
        sleep(5)

print("Complete")
