from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.CharField( max_length=10)
    title = models.CharField(max_length=50)

    body = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)

    edited_date = models.DateTimeField(default=timezone.now)

    def write(self):
        self.edited_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title