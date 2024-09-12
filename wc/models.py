from django.db import models

# Create your models here.
class blockboard(models.Model) :
    userid = models.IntegerField()
    mediaid = models.IntegerField()
    shared = models.BooleanField(default=False)

class auth(models.Model) :
    userid = models.IntegerField()
    token = models.TextField()
    verified = models.BooleanField(default=False)


    