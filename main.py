# yupi :)
import smtplib
from email.message import EmailMessage
from hidden import password, sender, reciever

# set your email and password
# please use App Password
#turn into array
email_address = sender
email_password = password

# create email
msg = EmailMessage()
msg['Subject'] = "Aquaphonics Garden Alert"
msg['From'] = email_address
msg['To'] = reciever
msg.set_content("System has detected a leak and both motors have been shut off")

# send email
with smtplib.SMTP_SSL('smtp-relay.sendinblue.com', 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)