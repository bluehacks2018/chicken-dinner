from django.contrib.postgres.fields import JSONField
from django.db import models

class DatasetManager(models.Manager):
    def get_feed(self):
        return self.all()

class Dataset(models.Model):
    name = models.CharField(max_length=200)
    rating = models.IntegerField()
    popularity = models.IntegerField()
    data = JSONField()
    objects = DatasetManager()
