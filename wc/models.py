from django.db import models

# Create your models here.
class Design(models.Model) :
    userId = models.IntegerField()
    list = models.TextField()

    