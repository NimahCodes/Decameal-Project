import random
import string
import threading

from django.core.mail import EmailMessage


class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data["email_subject"],
            body=data["email_body"],
            to=[data["to_email"]],
        )
        EmailThread(email).start()


class TicketNum:
    @staticmethod
    def create_ticket_number(num):
        return "00" + "".join(random.choice(string.digits) for i in range(num))
