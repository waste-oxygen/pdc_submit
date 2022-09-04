import json
import smtplib
from email.mime.text import MIMEText


profile = json.load(open("./profile.json"))
email_addressfrom = profile["email_addressfrom"]
email_addressto = profile["email_addressto"]
email_authcode = profile["email_authcode"]


def send_qqemail_to_myself(message, subject):
    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = email_addressfrom
        msg['To'] = email_addressto
        service = smtplib.SMTP_SSL("smtp.qq.com", 465)
        service.login(msg['From'], email_authcode)
        service.sendmail(msg['From'], msg['To'], msg.as_string())
        service.quit()
        return True
    except Exception:
        return False
