import smtplib  # https://docs.python.org/3/library/smtplib.html
import email  # https://docs.python.org/3/library/email.html
from app import config


# import smtpd
# need to turn on "less secure apps" in gmail
# https://myaccount.google.com/lesssecureapps


def send(message,subject=""):
    try:
        username = config.EMAIL_ADDR
        password = config.EMAIL_PASS
        with smtplib.SMTP('smtp.gmail.com', 587) as email_server:
            email_server.ehlo()
            email_server.starttls()
            email_server.login(user=username, password=password)
            email_server.sendmail(
                from_addr=config.EMAIL_ADDR,
                to_addrs=get_recipient(),
                msg=message,
                mail_options=[],
                rcpt_options=[],
            )

    except smtplib.SMTPException as e:
        print(e.strerror)


def receive():
    # https://codehandbook.org/how-to-read-email-from-gmail-using-python/
    pass


def get_recipient():
    addressee = [config.RECIPIENT]
    return addressee
