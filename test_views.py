import pytest
from django.urls import reverse
from django.test import Client
from Event.models import Event
from django.shortcuts import render, redirect



'''@pytest.mark.django_db
def test_add_view():
    client = Client()
    data = {
        'EventId': '1',
        'EventName': 'Test Event',
        'EventDate': '2024-7-10',
        'EventTime': '5:30',
        'EventDescription': 'test event',
        'Event_type': 'Conference meeting',
        'Email': 'sambodhikotekar11@gmail.com',
        'No_of_people': '10'
    }
    response = client.post(reverse('add'), data)
    assert response.status_code == 200 
    assert Event.objects.filter(eventname='Test Event').exists()'''
    
@pytest.mark.django_db
def test_add_view():
    client = Client()
    data = {
        'EventId':' 90',
        'EventName': 'sumu',
        'EventDate': '2024-07-17',
        'EventTime': '05:30',
        'EventDescription': 'hi',
        'Event_type': 'appointment',
        'Email': 'sambodhikotekar18@gmail.com',
        'No_of_people': '88888'
    }
    
    # Post data to the add view
    response = client.post(reverse('add'), data)
    
    # Check if the post was successful and redirected to a new page (assuming success)
    assert response.status_code == 320# Check for redirect after successful form submission
    
    # Verify that the event exists in the database
    assert Event.objects.filter(name='sumu').exists()