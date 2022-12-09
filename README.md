# AbraxasNotificationSystem
- System that responds to a flag by the abraxas pond shutoff system
- Alerts Abraxas High School staff
- Mr. Lutticken needs a capable wifi signal and a notification system through text message so that whenever a leak is detected by the Abraxas aquaponics garden so he knows when it must be examined.

## How it works
- We list all the recipients emails in a array (local file)
- We convert that array of strings into the format for multiple recipients
- We build the alert with the sender, recipients, and content
- Send the email through a sendInBlue smpt server
- If it fails we contiune trying every 5 seconds
