from django.db import models


class Motor(models.Model):
    name = models.CharField(max_length=1000)
    Temp = models.CharField(max_length=1000)
    voltage = models.CharField(max_length=1000)
    current = models.CharField(max_length=1000)
    speed = models.CharField(max_length=1000)
    vibrations = models.CharField(max_length=1000)




