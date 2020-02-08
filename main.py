from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import path

from requests import get
import smtplib
import settings as s


def main():
    IP = getIPAddress()
    compareIPAddress(IP)



def compareIPAddress(newIP):
    if path.exists("publicIP.txt"):
        print("Exists")
        f = open("publicIP.txt", "r")
        IP = f.read()
        print(IP)
        #If IP is not the same notify the user and write new ip to publicIP file
        if IP != newIP:
            message = "<html><body><p>Your Public IP address changed from " + IP + " to <b>" + newIP + ".</b></p></body></html>"
            f = open("publicIP.txt", "w")
            f.write(newIP)
            f.close()
            sendEmailMessage(message)

    else:
        #Init PublicIP file and send new ip to file and send mail to user
        f = open("publicIP.txt", "w")
        f.write(newIP)
        f.close()
        message = "<html><body><p>Your Public IP address is <b>" + newIP + ".</b></p></body></html>"
        sendEmailMessage(message)


def getIPAddress():
    #Get public IP address
    ip = get('https://api.ipify.org').text
    print('My public IP address is:', ip)
    return ip


def sendEmailMessage(message):
    #Send Mail
    print("Creating Email")
    fromaddr = s.EMAIL 
    toaddr = s.RECIEVER
    msg = MIMEMultipart('alternative')
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "IP Changed"
    server = smtplib.SMTP_SSL(s.SERVERURL, s.SERVERPORT)
    server.set_debuglevel(0)
    server.login(s.EMAIL, s.EMAILPASSWORD)
    msg.attach(MIMEText(message, 'html'))
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print("Email Send")


if __name__ == "__main__":
    main()
