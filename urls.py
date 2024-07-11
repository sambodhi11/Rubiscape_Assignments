"""
URL configuration for NewEventSecheduler project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Event import views
from celery import Celery
from Event import remediation


urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.index, name='index'),
    path('add/',views.add, name='add'),
    path('display/',views.display, name='display'),
    path('Update/',views.Update,name='Update'),
    path('test/',views.test,name='test'),
    path('sendmail/',views.send_mail_to_all,name='sendmail'),
    path('delete/',views.delete, name='delete'),
   
]
