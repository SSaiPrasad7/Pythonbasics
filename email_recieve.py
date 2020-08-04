import email
import imaplib
imap_server=imaplib.IMAP4_SSL('imap.gmail.com',993)
email_address="samudralasai1999@gmail.com"
password=input('Enter password: ')
imap_server.login(email_address,password)
imap_server.select("inbox")
_, search_data = imap_server.search(None, 'ALL')
my_message = []
for num in search_data[0].split():
    email_data = {}
    _, data = imap_server.fetch(num, '(RFC822)')
    _, b = data[0]
    email_message = email.message_from_bytes(b)
    for header in ['subject', 'to', 'from', 'date']:
        print("{}: {}".format(header, email_message[header]))
        email_data[header] = email_message[header]
    for part in email_message.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            email_data['body'] = body.decode()
        elif part.get_content_type() == "text/html":
            html_body = part.get_payload(decode=True)
            email_data['html_body'] = html_body.decode()
    my_message.append(email_data)
    print(my_message)

