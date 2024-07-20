from django.db import models

class Scooter(models.Model):
    name = models.IntegerField(max_length=55)
