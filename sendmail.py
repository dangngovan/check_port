#!/usr/bin/python
# -*- coding: utf8 -*-
import smtplib
import sys
def sendmail(i):
	FROM = "dangngovan@cnht.vn"
  	TO = ['IT-Hanoi@vccorp.vn' ,'quangngovinh@vccorp.vn','dungtrantrung@vccorp.vn','dangngovan@vccorp.vn']
	SUBJECT = "KIỂM TRA KẾT NỐI VN MÁY CHẤP CÔNG  %s"%i
	BODY = "Admin kiểm tra khi nhận được thông báo này!!!"
	msg = """\
From: %s
To: %s
Subject: %s
%s
"""%(FROM,", ".join(TO), SUBJECT, BODY)
	server = smtplib.SMTP('mail.cnht.vn', 587)
	server.starttls()
	server.login("*****", "******")
	server.sendmail(FROM, TO, msg)
	server.quit()
if __name__ == "__main__":
    sendmail(sys.argv[1])
