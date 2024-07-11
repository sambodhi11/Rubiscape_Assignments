from django.db import models

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    event_type = models.TextField(null=True)  
    email=models.EmailField(null=True)
    no_of_people= models.IntegerField(null=True)

    def __str__(self):
        return f"{self.id},{self.name},{self.date},{self.time},{self.description},{self.event_type},{self.email},{self.no_of_people}"


