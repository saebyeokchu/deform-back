from django.db import models

# Create your models here.
class blockboard(models.Model) :
    userid = models.IntegerField()
    mediaid = models.IntegerField()
    shared = models.BooleanField(default=False)


    