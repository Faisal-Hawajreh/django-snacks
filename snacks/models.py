from django.db import models

# Create your models here.
# when you name your model ,it should be a singular.
class Snack(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

# Don't forget to add your app to settings file (installed app list)
# Don't forget to register your app in admin file

class SpicySnack(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    spicy = models.BooleanField()

    def __str__(self):
        return self.name
