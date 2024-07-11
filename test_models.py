import pytest
from datetime import date, time
from Event.models import Event
from django.db import models

'''@pytest.mark.django_db
def test_create_event():
    event = Event.objects.create(
        id=1,
        name="Test Event",
        date=date(2024, 7, 10),
        time=time(5, 30),
        description='TEST',
        event_type= 'Meeting',
        email ='sambodhikotekar11@gmail.com',
        no_of_people =10
    )
    assert event.pk'''

@pytest.mark.django_db
def test_event_creation():
    # Create a new Event instance
    event = Event.objects.create(
        id= 90,
        name='sumu',
        date=date(2024, 7, 17),
        time=time(5, 30),
        description='hi',
        event_type='appointment',
        email='sambodhikotekar18@gmail.com',
        no_of_people= 88888
    )
    
    # Retrieve the event from the database
    saved_event = Event.objects.get(pk=event.pk)
    
    # Assert that the saved event matches the created data
    assert saved_event.id == 90
    assert saved_event.name == 'sumu'
    assert saved_event.date == date(2024, 7, 17)
    assert saved_event.time == time(5, 30)
    assert saved_event.description == 'hi'
    assert saved_event.event_type == 'appointment'
    assert saved_event.email == 'sambodhikotekar18@gmail.com'
    assert saved_event.no_of_people == 88888

def test_event_str_method():
    # Create an Event instance
    event = Event(
        id= 90,
        name='sumu',
        date=date(2024, 7, 17),
        time=time(5, 30),
        description='hi',
        event_type='appointment',
        email='sambodhikotekar18@gmail.com',
        no_of_people=88888
    )
    
    # Assert that the __str__() method returns the expected string format
    assert str(event) == "90,sumu,2024-07-17,05:30:00,hi,appointment,sambodhikotekar18@gmail.com,88888"