from django.db import models

# Create your models here.

class Engine(models.Model):
    name = models.CharField('engine name', max_length=200)
    slug = models.CharField('engine slug', max_length=200)
    
    pub_date = models.DateTimeField('date published')
    dictionary = models.TextField(default='')
    sample = models.TextField(default='')
    def __str__(self):
        return self.name