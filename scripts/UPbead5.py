#!/usr/bin/perl
import sys;

def sendMail(host, addr, to, subject, content):
    print "Level kuldese : ";
    import smtplib
    from email.MIMEText import MIMEText

    server = smtplib.SMTP(host)
    msg    = MIMEText(content)

    msg["Subject"] = subject
    msg["From"]    = addr
    msg["To"]      = to

    server.sendmail(addr, [to], msg.as_string())
    server.quit()
    print "SIKERES.";

def read_msg(host, addr, to, subject):
    print "Udv";
    print "Felado : ",addr; 
    print "Cimzett : ",to;
    print "Targy : ",subject,"\n";
    print "Uzeneted : ";
    content = raw_input();
    sendMail(host, addr, to, subject, content);

sender = 'valami@inf.elte.hu';
read_msg('mail.elte.hu',sender,sys.argv[1],sys.argv[2]);
