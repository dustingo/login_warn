#!/usr/bin/env python3
#! -*- coding:utf-8 -*-
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from mailconfig import mailinfo

def send_email(mailtext):
	msg = MIMEText(mailtext,'html','utf-8')
	msg['From'] = u'<%s>' % mailinfo["from_address"]
	msg['To'] = u'<%s>' % mailinfo["to_address"]
	msg['Subject'] = u"登陆警告"

	smtp = smtplib.SMTP_SSL('smtp.163.com', 465)
	smtp.set_debuglevel(0)
	smtp.ehlo("smtp.163.com")
	smtp.login(mailinfo["from_address"], mailinfo["from_pass"])
	smtp.sendmail(mailinfo["from_address"], [mailinfo["to_address"]], msg.as_string())
	smtp.quit()
