from django.db import models
from django.contrib.postgres.fields import ArrayField

class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add = True)
    photos = ArrayField(models.CharField(max_length=300), null=True, blank=True, size=3)