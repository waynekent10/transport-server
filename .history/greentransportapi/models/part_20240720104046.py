from django.db import models

class Part(models.Model):
  part_name = models.TextField()
  part_number = models.IntegerField()
