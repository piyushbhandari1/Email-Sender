import smtplib

sender = ""
receiver = ""
password = ""
subject = "python email test"
body = " I wrote an email from myself to myself. :D "


message = f"""From: Snoop Dogg{sender}
To: Nicholas cage{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
try:
    server.login(sender,password)
    print("logged in...")
    server.sendmail(sender,receiver,message)
    print("Email Sent! ")

except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")