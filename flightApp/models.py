from tkinter import CASCADE
from django.db import models

from core.models import TimeStampModel


class Flight(TimeStampModel):
    flightNumber             = models.CharField(max_length=10)
    operatingAirline         = models.CharField(max_length=20)
    departureCity            = models.CharField(max_length=20)
    arriveCity               = models.CharField(max_length=20)
    dateOfDeparture          = models.DateField()
    estimatedTimeOfDeparture = models.DateTimeField()


class Passenger(TimeStampModel):
    firstName = models.CharField(max_length=20)
    lastName  = models.CharField(max_length=20)
    email     = models.CharField(max_length=20)
    phone     = models.CharField(max_length=20)


class Reservation(TimeStampModel):
    flight    = models.ForeignKey('Flight', on_delete=models.CASCADE)
    passenger = models.OneToOneField('Passenger', on_delete=models.CASCADE)