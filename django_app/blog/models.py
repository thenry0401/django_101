from django.db import models


# Create your models here.
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')

    title = models.CharField(max_length=200)

    text = models.TextField()

    created_date = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return self.title
