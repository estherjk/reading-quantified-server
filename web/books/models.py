from django.contrib.postgres.fields import JSONField
from django.db import models

class Genre(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=20, unique=True)
    trello_id = models.CharField(max_length=36, unique=True)
    color = models.CharField(max_length=12, default='')

    def __str__(self):
        return '%s' % (self.name)

class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=128)
    trello_id = models.CharField(max_length=36, unique=True)
    date_started = models.DateTimeField()
    date_finished = models.DateTimeField()
    genres = models.ManyToManyField(Genre)
    cover_attachment = JSONField(default=dict, blank=True, help_text='Trello card attachment info. See https://developers.trello.com/reference#cardsidattachments.')