import smtplib
import ssl

port = 587
smtp_server = "smtp.gmail.com"
sender_email='samudralasai1999@gmail.com'
password=input('Enter password: ')

receiver_email=input('Enter the Receiver mail id ')
subject_line = input('Enter the subject line:')
body = input('Enter the message: ')
message = "Subject: " + subject_line + "\n" + body
context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print("sent")

#cndtnnrynyrvteea