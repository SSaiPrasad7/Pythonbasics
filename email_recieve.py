import email
import imaplib
imap_server=imaplib.IMAP4_SSL('imap.gmail.com')
email_address="samudralasai1999@gmail.com"
password=input('Enter password: ')
imap_server.login(email_address,password)
imap_server.select('inbox')
type,data=imap_server.search(None,'SUBJECT "test"')
email_id=data[0]
result,email_data=imap_server.fetch(email_id,'(RFC822)')
raw_email=email_data[0][1].decode('utf-8')
email_message=email.message_from_bytes(raw_email)
for part in email_message.walk():
    if part.get_content_type()=='text/plain':
        body=part.get_payload(decode=True)
        print(body)

