'''from .models import Event
from django.shortcuts import render
from django.http import HttpResponse


def update_emails(request):
    default_email = "default@gmail.com"
    events = Event.objects.all()
    updated = False

    for event in events:
        if event.user.mail is None:
            event.user.mail = default_email
            event.save()
            updated = True

    if updated:
        return HttpResponse("Emails updated.")
    else:
        return HttpResponse("All emails are already filled.")
    
    
def update_emails(request):
    default_email = "default@gmail.com"
    events = Event.objects.filter(user_mail__isNone=True)

    for event in events:
        event.user_mail = default_email
        event.save()

    if events.exists():
        return HttpResponse("Emails updated.")
    else:
        return HttpResponse("All emails are already filled.")'''

from .models import Event
from django.shortcuts import render
from django.http import HttpResponse


def update_emails(request):
    default_email ="default@gmail.com"
    event =Event.objects.all()
    
    for event in Event:
        if Event.email is None:
            Event.email =default_email
            event.save()
            return HttpResponse("Sent")
        else:
            return HttpResponse("Already sent")
        
