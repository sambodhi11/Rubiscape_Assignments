'''from __future__ import absolute_import, unicode_literals
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task

@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "done"

@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = "Event Reminder "
        message = "Hello, This mail is to give you a reminder of your schedule."
        to_email = user.email
    try:
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=False,
        )
    except Exception as error:
            print(f"Failed to send email to {user.email}: {str(error)}")
    return "done"'''

from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings

@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "done"
    
@shared_task(bind=True)
def send_mail_func(self, email, event_name, event_date, event_time):
    mail_subject = f"Event Confirmation: {event_name}"
    message = f"Hello, this is a confirmation for your event '{event_name}' scheduled on {event_date} at {event_time}."
    
    try:
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )
    except Exception as error:
        print(f"Failed to send email to {email}: {str(error)}")
    
    return "done"

