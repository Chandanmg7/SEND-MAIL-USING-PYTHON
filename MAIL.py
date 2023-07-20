import smtplib

gmail_user = 'GMAIL'
gmail_password = '#####-----APP-PASSWORD---#####'

sent_from = gmail_user
to = ['GMAIL']
subject = 'MDT720919MDT'
body = 'MDT'

email_text = """TEXT
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)





    