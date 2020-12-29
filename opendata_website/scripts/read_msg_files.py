from outlook_msg import Message
from os import listdir
from os.path import isfile, join
import sys

mypath = sys.argv[1]

for fname in [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith('msg')]:
    with open(fname) as msg_file:
        msg = Message(msg_file)

    # Contents are the plaintext body of the email
    contents = msg.body
    print(contents)
    # Attachments can be read and saved like so
    #first_attachment = msg.attachments[0]
    #with first_attachment.open() as attachment_fp, open(first_attachment.filename, 'wb') as output_fp:
    #    output_fp.write(attachment_fp.read())