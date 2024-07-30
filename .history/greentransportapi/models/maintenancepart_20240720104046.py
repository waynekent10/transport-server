from django.db import models
from .maintanance import Maintenance
from .part import Part

class Maintenance_part(models.Model):
 Maintenance_id = models.ForeignKey(Maintenance, on_delete=models.CASCADE)
 part_id = models.ForeignKey(Part, on_delete=models.CASCADE)
