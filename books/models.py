from django.db import models

class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    date_started = models.DateTimeField()
    date_finished = models.DateTimeField()