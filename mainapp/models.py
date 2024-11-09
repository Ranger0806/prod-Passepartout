from django.db import models
from firstapp.models import ProjectUser

class Tickets(models.Model):
    user = models.ForeignKey(ProjectUser, on_delete=models.CASCADE)
    date = models.DateField()
    country = models.CharField(max_length=50)

class Files(models.Model):
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    file = models.BinaryField()
