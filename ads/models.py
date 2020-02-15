from django.db import models
from django.contrib.postgres.fields import ArrayField

# class AdManager(models.Manager):
#     def new (self):
#         return self.order_by('-date')
#     def cost (self):
#         return self.order_by('-price')

class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add = True)
    photos = ArrayField(models.CharField(max_length=300), null=True, blank=True, size=3)
    # def __str__(self):
    #     return self.title
    # def get_url(self):
    #     return reverse('question_details', kwargs = {'pk': self.pk})
    class Meta:
        ordering = ['date']