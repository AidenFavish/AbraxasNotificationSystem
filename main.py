# yupi :)
import smtplib
from email.message import EmailMessage

# set your email and password
# please use App Password
email_address = "aidenfavish@gmail.com"
email_password = "GE9KdsVDNxH3kySg"

# create email
msg = EmailMessage()
msg['Subject'] = "Aquaphonics Garden Alert"
msg['From'] = email_address
msg['To'] = "8582659484@txt.att.net"
msg.set_content("System has detected a leak and both motors have been shut off")

# send email
with smtplib.SMTP_SSL('smtp-relay.sendinblue.com', 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)