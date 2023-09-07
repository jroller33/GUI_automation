import smtplib
import ssl
from email.message import EmailMessage

email_sender = 'ShunticiaR@gmail.com'
email_password = 'mfxxjlbrdctlvgzx'
email_receivers = ['jtroller33@gmail.com', 'ktyson8@gmail.com', 'gtyson12@gmail.com']

subject = "Hi! I'm MAnnBot!"
body = """
Hello. My name is MAnnBot.

I am a bot that was created by Shunticia R. and Dr. Satrantha Roller, M.D., to provide continuous monitoring and reporting of MAnn's personal income. I will automatically deliver convenient bi-monthly updates directly to you, free of charge. This highly commodious bot was made possible by a grant from the NSA and FBI, due to their unwavering interest in MAnn's personal life.

In August, 2023, MAnn had the following gross income:

Date:             Gross Income Amount:            Transaction Number:
08/01/2023            $1,824.50                     JV 006 SAR05927008	
08/15/2023            $1,824.50                     JV 006 SAR05934009	

Total Gross Income:   $3,649.00

Be sure to check your email again next month for more updates!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = ", ".join(email_receivers)
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receivers, em.as_string())