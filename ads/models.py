from django.db import models

class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Photo(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField()

    def __str__(self):
        return self.ad.title