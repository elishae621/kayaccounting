from simple_mail.mailer import BaseSimpleMail, simple_mailer

class Mail(BaseSimpleMail):
    email_key = 'Mail'


simple_mailer.register(Mail)