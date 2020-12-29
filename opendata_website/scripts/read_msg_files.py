from outlook_msg import Message
from os import listdir
from os.path import isfile, join
import sys

emails = []

mypath = sys.argv[1]

for fname in [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith('msg')]:
    with open(fname) as msg_file:
        msg = Message(msg_file)

    # Contents are the plaintext body of the email
    try:
        sender_email = msg.sender_email
    except:
        sender_email = ''
    email = {'sender_email': sender_email, 'body': msg.body, 'subject': msg.subject, 'attachment_file_names': [attachment.filename for attachment in msg.attachments]}
    emails.append(email)
    # Attachments can be read and saved like so
    #first_attachment = msg.attachments[0]
    #with first_attachment.open() as attachment_fp, open(first_attachment.filename, 'wb') as output_fp:
    #    output_fp.write(attachment_fp.read())

print(emails)