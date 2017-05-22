import smtplib

from email.mime.text import MIMEText

msg = MIMEText('Testing some Mailgun awesomness')
msg['Subject'] = "Hello"
msg['From']    = "postmaster@appd2cb3ded4cdf448c8c29b5d31a03d4b1.mailgun.org"
msg['To']      = "v.a.stpnv@yandex.ru"

s = smtplib.SMTP('smtp.mailgun.org', 587)

s.login('postmaster@appd2cb3ded4cdf448c8c29b5d31a03d4b1.mailgun.org', 'e174d564f9ebf115e74636f58e4ff15c')
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()