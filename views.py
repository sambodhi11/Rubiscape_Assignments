from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.db import IntegrityError 
from .models import Event
from .task import send_mail_func , test_func
from datetime import datetime, timedelta
from django.utils import timezone


def index(request):
    return render(request, 'index.html')
    
def add(request):
    context = {"data": Event.objects.all()}
    
    if request.method == 'POST':
        events_id = request.POST.get('EventId')
        events_name = request.POST.get('EventName')
        events_date = request.POST.get('EventDate')
        events_time = request.POST.get('EventTime')
        events_description = request.POST.get('EventDescription')
        event_type = request.POST.get("Event_type")
        events_email = request.POST.get("Email")
        no_of_people = request.POST.get("No_of_people")
         
        if not all([events_id, events_name, events_date, events_time, events_description, event_type, events_email, no_of_people]):
            context['error'] = "All fields are required."
            return render(request, 'add.html', context)
        
        try:
            event_date = datetime.strptime(events_date, "%Y-%m-%d").date()
            if event_date < timezone.now().date():
                context['error'] = "Event date must be today or in the future."
                return render(request, 'add.html', context)
            
            new_event = Event(
                id=events_id,
                name=events_name, 
                date=events_date, 
                time=events_time, 
                description=events_description, 
                event_type=event_type, 
                email=events_email,
                no_of_people=no_of_people
            )
            new_event.save()
            
            # Send confirmation email
            send_mail_func(events_email, events_name, events_date, events_time)

            # Schedule reminder email one day before the event
            reminder_time = datetime.combine(event_date - timedelta(days=1), datetime.strptime(events_time, "%H:%M").time())
            send_mail_func.apply_async((events_email, events_name, events_date, events_time), eta=reminder_time)
            
            return redirect('display')
            
        except IntegrityError:
            context['error'] = "Error adding the event. Please try again."
            return render(request, 'add.html', context)
    
    return render(request, 'add.html', context)

def display(request):
    events = Event.objects.all()
    return render(request, 'display.html', {'events': events})

def Update(request):
    if request.method == 'POST':
        event_id = request.POST.get("Event_Id")
        name = request.POST.get('Eventname')
        date = request.POST.get('EventDate')
        time = request.POST.get('EventTime')
        description = request.POST.get('EventDescription')
        event_type = request.POST.get('event_type')
        email = request.POST.get("Email")
        no_of_people=request.POST.get("no_of_people")

        try:
            event = Event.objects.get(id=event_id)
            if name:
                event.name = name
            if date:
                event.date = date
            if time:
                event.time = time
            if description:
                event.description = description
            if event_type:
                event.event_type = event_type
            if event.email:
                event.email=email
            if no_of_people:
                event.no_of_people =int (no_of_people)
            event.save()

            return redirect('display')

        except Event.DoesNotExist:
            error = "Event does not exist."
        return render(request, 'Update.html', {'error': error})

    return render(request, 'Update.html')

def delete(request):
    if request.method == 'POST':
        e_id = request.POST.get('EventId') 
        try:
            event = Event.objects.get(id=e_id)
            event.delete()
            return redirect('display') 
        except Event.DoesNotExist:
            error = "Name does not exist."
            
            return render(request, 'delete.html', {'error': error})
      
    return render(request, 'delete.html')


def update_emails(request):
    default_email = "default@gmail.com"
    events = Event.objects.filter(email__isnull=True)

    for event in events:
        event.email = default_email
        event.save()

    if events.exists():
        return HttpResponse("Emails updated.")
    else:
        return HttpResponse("All emails are already filled.")

'''def remediation(request):
    events = Event.objects.all()

    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        description = request.POST.get('description')
        event_type = request.POST.get('event_type')
        email =request.POST.get('email')
        no_of_people=request.POST.get('no_of_people')
        Event.objects.create(
            id=id,
            name=name,
            date=date,
            time=time,
            description=description,
            event_type=event_type,
            email=email,
            no_of_people=no_of_people
        
        )

    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'remediation.html', context)'''
   
def test(request):
    test_func.delay()
    return HttpResponse('Test done!')

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("The mail is sent.Thank you.")


