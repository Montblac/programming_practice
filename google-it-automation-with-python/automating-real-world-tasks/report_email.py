#!/usr/bin/env python3
import os
import datetime
import reports
import emails

if __name__ == '__main__':
    dir = 'supplier-data/descriptions'
    files = os.listdir(dir)
    paragraph = ''

    for file in files:
        path = os.path.join(dir, file)
        with open(path) as f:
            content = f.readlines()
            name, weight = content[:2]
            paragraph += 'name: {}<br/>weight: {}<br/><br/>'.format(name, weight)

    date = datetime.datetime.now()
    title = 'Processed Update on {}'.format(date.strftime('%B %d, %Y'))
    attachment = '/tmp/processed.pdf'
    reports.generate_report(attachment, title, paragraph)


    sender      = 'automation@example.com'
    recipient   = '{}@example.com'.format(os.environ.get('USER'))
    subject     = 'Upload Completed - Online Fruit Store'
    body        = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    attachment  = '/tmp/processed.pdf'

    message = emails.generate_email(sender, recipient, subject, body, attachment)
    emails.send_email(message)
