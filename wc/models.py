from django.db import models

# Create your models here.
class Design(models.Model) :
    userid = models.IntegerField()
    mediaid = models.IntegerField()
    shared = models.BooleanField()
    createdat = models.DateTimeField()

    