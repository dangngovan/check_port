import smtplib
import sys
def sendmail(i):
	FROM = "*****"
  TO = ['******']
	SUBJECT = "CANH BAO MAY CHAM CONG %s"%i
	BODY = "Admin kiem tra may cham cong khi nhan duoc canh bao nay!!!"
	msg = """\
From: %s
To: %s
Subject: %s
%s
"""%(FROM,", ".join(TO), SUBJECT, BODY)
	server = smtplib.SMTP('mail.cnht.vn', 587)
	server.starttls()
	server.login("*****@****.vn", "******")
	server.sendmail(FROM, TO, msg)
	server.quit()
if __name__ == "__main__":
    sendmail(sys.argv[1])
