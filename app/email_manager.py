import smtplib  # https://docs.python.org/3/library/smtplib.html
import imaplib  # https://codehandbook.org/how-to-read-email-from-gmail-using-python/
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# https://docs.python.org/3/library/email.html
from app import config


# import smtpd
# need to turn on "less secure apps" in gmail
# https://myaccount.google.com/lesssecureapps


def send(recipient, message, subject=""):
    try:
        username = config.EMAIL_ADDR
        password = config.EMAIL_PASS
        with smtplib.SMTP('smtp.gmail.com', 587) as email_server:
            email_server.ehlo()
            email_server.starttls()
            email_server.login(user=username, password=password)
            email_server.sendmail(
                from_addr=config.EMAIL_ADDR,
                to_addrs=recipient,
                msg=message,
                mail_options=[],
                rcpt_options=[],
            )

    except smtplib.SMTPException as e:
        print(e.strerror)


def receive():
    username = config.EMAIL_ADDR
    password = config.EMAIL_PASS
    server = "imap.gmail.com"
    port = 993

    mail = imaplib.IMAP4_SSL(server)
    mail.login(username, password)
    mail.select('inbox')


def send_email(recipient, message_string, subject=""):

    try:
        username = config.EMAIL_ADDR
        password = config.EMAIL_PASS
        with smtplib.SMTP('smtp.gmail.com', 587) as email_server:
            message = MIMEMultipart("alternative")
            message['subject'] = subject
            message['from'] = config.EMAIL_ADDR
            message["to"] = recipient
            message.attach(MIMEText(message_string, 'plain'))
            email_server.ehlo()
            email_server.starttls()
            email_server.login(user=username, password=password)
            email_server.sendmail(
                from_addr=config.EMAIL_ADDR,
                to_addrs=recipient,
                msg=message.as_string(),
                mail_options=[],
                rcpt_options=[],
            )

    except smtplib.SMTPException as e:
        print(e.strerror)
