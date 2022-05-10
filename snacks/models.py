from pydoc import describe
from django.db import models

# Create your models here.
# when you name your model ,it should be a singular.
class Snack(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

# Don't forget to add your app to settings file (installed app list)