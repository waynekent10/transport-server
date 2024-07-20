from django.db import models
from .maintenance import Maintenance
from .part import Part

class MaintenancePart(models.Model):
 maintenance = models.ForeignKey(Maintenance, on_delete=models.CASCADE)
 part = models.ForeignKey(Part, on_delete=models.CASCADE)
