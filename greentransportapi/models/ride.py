from django.db import models
from .user import User
from .scooter import Scooter

class Ride(models.Model):
    user = models.ForeignKey(User, related_name='rides', on_delete=models.CASCADE)
    scooter = models.ForeignKey(Scooter, on_delete=models.CASCADE)
    duration = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ride by {self.user.username} on {self.scooter} for {self.duration} minutes"
