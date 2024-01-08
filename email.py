import getpass
import smtplib

HOST='smtp-mail.outlook.com'
PORT=587

FROM_EMAIL="syedfawazali@outlook.com"
TO_EMAIL="fawaz.exe@gmail.com"
PASSWORD=getpass.getpass('Enter Password: ')

MESSAGE= """
Subject: Mail sent using Py

Hi, There are better times coming!
"""

smtp = smtplib.SMTP(HOST,PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code}{response}")

status_code,response = smtp.starttls()
print(f"[*] Starting TLS Connection: {status_code}{response}")

status_code,response = smtp.login(FROM_EMAIL,PASSWORD)
print(f"[*] Logging in: {status_code}{response}")

smtp.sendmail(FROM_EMAIL,TO_EMAIL,MESSAGE)
# smtp.send
smtp.quit()