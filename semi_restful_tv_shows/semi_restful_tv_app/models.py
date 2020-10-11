from __future__ import unicode_literals
from django.db import models
# Our custom manager!
# No methods in our new manager should ever receive the whole request object as an argument! 
# (just parts, like request.POST)
class ShowManager(models.Manager):
    def create_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        return errors
# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()