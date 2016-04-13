from django.db import models
from greeter.models import Member


class Room(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)


class Booking(models.Model):
    user = models.ForeignKey(Member)
    start = models.DateTimeField()
    end = models.DateTimeField()
    all_day = models.BooleanField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    was_cancelled = models.BooleanField()
