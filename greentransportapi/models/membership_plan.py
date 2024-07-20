from django.db import models

class MembershipPlan(models.Model):
    plan_name = models.CharField(max_length=255)
    monthly_cost = models.IntegerField()
