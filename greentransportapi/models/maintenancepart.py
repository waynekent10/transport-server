from django.db import models
from .maintenance import Maintenance
from .part import Part

class MaintenancePart(models.Model):
 Maintenance_id = models.ForeignKey(Maintenance, on_delete=models.CASCADE)
 part_id = models.ForeignKey(Part, on_delete=models.CASCADE)
