#!/usr/bin/python
#coding:utf-8
import smtplib
from email.mime.text import MIMEText
import sys
mail_host = 'smtp.qq.com'
mail_user = '907708051@qq.com'
mail_pass = 'tkjftoadiffpbbei'
def send_mail(to_list,subject,content):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = mail_user
    msg['to'] = to_list
    try:
        s = smtplib.SMTP_SSL()
        s.connect(mail_host,465)
        s.login(mail_user,mail_pass)
        s.sendmail(mail_user,to_list,msg.as_string())
        s.close()
        return True
    except Exception,e:
        print str(e)
        return False
if __name__ == "__main__":
    send_mail(sys.argv[1], sys.argv[2], sys.argv[3])
