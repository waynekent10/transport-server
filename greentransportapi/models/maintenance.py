from django.db import models
from .scooter import Scooter

class Maintenance(models.Model):
    scooter = models.ForeignKey(Scooter, on_delete=models.CASCADE)
    maintenance_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
