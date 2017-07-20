# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from subprocess import check_output
class Email_server(object):
    mail_host = "smtp.qq.com"
    mail_user = '2498596694@qq.com'
    mail_pass = "zinlwkbkgkthecca"
    def __init__(self,receivers,subject,text):
        self.receivers=receivers
        self.subject=subject
        self.text=text
    def info(self):
        message = MIMEText(self.text)
        message['From'] = Header(self.mail_user, 'utf-8')
        message['To'] = Header(str(self.receivers), 'utf-8')
        subject =self.subject
        message['Subject'] = Header(subject, 'utf-8')
        return message
    def send(self):
        try:
            smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)
            smtpObj.login(self.mail_user, self.mail_pass)
            message=self.info()
            smtpObj.sendmail(self.mail_user, self.receivers, message.as_string())
            smtpObj.quit()
            print "邮件发送成功"
        except smtplib.SMTPException, e:
            print str(e)

if __name__=='__main__':
    email_test=Email_server(['2664074035@qq.com','2498596694@qq.com'],"南京美食","汤包，盐水呀，蒸饺")
    email_test.send()

