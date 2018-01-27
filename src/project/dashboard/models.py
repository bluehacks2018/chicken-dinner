from django.contrib.postgres.fields import JSONField
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

class DatasetManager(models.Manager):
    def get_feed(self):
        tags = user.tags.all()
        datasets = self.filter(tags=tags).order_by('score')

        return datasets

class Dataset(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=300, null=True)
    description = models.TextField(null=True)
    rating = models.IntegerField(default=0)
    popularity = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    data = JSONField(
        default={
            'labels':'None',
            'series': 'None',
            }
        )
    tags = models.ManyToManyField(Tag)
    
    objects = DatasetManager()
