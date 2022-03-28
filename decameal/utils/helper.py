import random
import string

from django.core.mail import EmailMessage


class Helper:
    def generate_OTP(num):
        return "".join(random.choice(string.digits) for i in range(num))

    def send_mail(data):
        email = EmailMessage(
            subject=data["email_subject"],
            body=data["email_body"],
            to=[data["to_email"]],
        )
        email.send()
