from django.db import models

# Create your models here.
class blockboard(models.Model) :
    userid = models.IntegerField()
    mediaid = models.IntegerField()
    postid = models.IntegerField(null=True)
    shared = models.BooleanField(default=False)
    productid = models.IntegerField(null=True)

class auth(models.Model) :
    userid = models.IntegerField()
    token = models.TextField()
    verified = models.BooleanField(default=False)


    