# # watch out for googling the things you google may be outdated

# # https://docs.python.org/3/library/email.examples.html
# # https://docs.python.org/3/library/email.html#module-email
# # https://www.geeksforgeeks.org/simple-mail-transfer-protocol-smtp/

# import smtplib
# from email.message import EmailMessage

# # to send emails you need a server - this is done through smtp
# # standard for emails to be sent from computer to computer
# email = EmailMessage()
# email["from"] = "Maria Claydon"
# email["to"] = "claydonmaria@gmail.com"
# email["subject"] = " You won 1,000,000 dollars!"

# email.set_content("I am a Python Master")

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     # serverPW = "qszplvznnetuhgcl"
#     smtp.ehlo()
#     # hello this is a server I am awake message
#     smtp.starttls()
#     # tls = enxryption mechanism - connect securely to the server
#     smtp.login("mariatestingpython@gmail.com", "csvr nnud gpsb gmuh")
#     # connect to your email account
#     smtp.send_message(email)
#     print("all good boss")

import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "Maria Claydon"
email["to"] = "mariatestingpython@gmail.com"
email["subject"] = "You won 1,000,000 dollars!"
email.set_content("I am unstoppable")

with smtplib.SMTP(host="smtp.gmail.com", port=486) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("mariatestingpython@gmail.com", "tlqouquytdjberpd")
    smtp.send_message(email)
    print("All good boss")
