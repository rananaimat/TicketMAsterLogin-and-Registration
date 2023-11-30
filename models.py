from django.db import models

# Create your models here.
class TicketMaster(models.Model):
    email = models.EmailField()
    password = models.TextField()
