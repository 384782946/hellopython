# -*-coding:utf-8 -*
'''
Created on 2016年3月8日

@author: zxj
'''

import smtplib
from smtplib import SMTPException
from email.mime.text import MIMEText

def send_email(sender,passwd,receivers,title,message):
    try:
        msg = MIMEText(message,'html','utf-8')
        msg['subject'] = title
        msg['from'] = sender
        msg['to'] = receivers
        
        smtpObj = smtplib.SMTP('smtp.163.com',25)
        #smtpObj.connect('smtp.163.com',25)
        smtpObj.login(sender, passwd)
        smtpObj.sendmail(sender,receivers,msg.as_string())
        smtpObj.quit()
        print 'success'
    except SMTPException , e:
        print str(e)
    finally:
        pass

if __name__ == "__main__":
    usr = raw_input('Input your 163 emial user name:')
    psw = raw_input('Input your password:')
    title = raw_input('Input your emial subproject:')
    to  = raw_input('Input emial you send to:')
    send_email(usr,psw,to,title,'<html><h1>你好,我在用ptyhon发邮件</h1></html>')