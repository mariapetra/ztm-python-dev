# # watch out for googling the things you google may be outdated

# # https://docs.python.org/3/library/email.examples.html
# # https://docs.python.org/3/library/email.html#module-email
# # https://www.geeksforgeeks.org/simple-mail-transfer-protocol-smtp/
# https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email["from"] = "Maria Claydon"
email["to"] = "mariatestingpython@gmail.com"
email["subject"] = "You won 1,000,000 dollars!"
email.set_content(html.substitute({name: 'tintin'}), 'html')

with smtplib.SMTP(host="smtp.gmail.com", port=486) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("mariatestingpython@gmail.com", "tlqouquytdjberpd")
    smtp.send_message(email)
    print("All good boss")
