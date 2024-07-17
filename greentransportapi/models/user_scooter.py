from django.db import models
from .user import User
from .scooter import Scooter

class UserScooter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scooter = models.ForeignKey(Scooter, on_delete=models.CASCADE)
