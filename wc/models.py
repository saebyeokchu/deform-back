from django.db import models

# Create your models here.
class Product(models.Model) :
    price = models.IntegerField()

class Post(models.Model) :
    title = models.TextField()
    status = models.TextField()
    content = models.TextField()
    categories = models.IntegerField()

    