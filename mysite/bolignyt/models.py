
from django.db import models

# Create your models here.

class PythonBolig(models.Model):
    date_found = models.DateTimeField(max_length=500, null=True, blank=True)
    Price = models.CharField(max_length=500)
    Url = models.CharField(max_length=500)
    Description = models.CharField(max_length=500)


    def __unicode__(self):
        return self.title
