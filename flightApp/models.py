from django.db                import models
from django.db.models.signals import post_save
from django.dispatch          import receiver
from django.conf              import settings

from rest_framework.authtoken.models import Token

from core.models import TimeStampModel


class Flight(TimeStampModel):
    flightNumber             = models.CharField(max_length=10)
    operatingAirline         = models.CharField(max_length=20)
    departureCity            = models.CharField(max_length=20)
    arriveCity               = models.CharField(max_length=20)
    dateOfDeparture          = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()


class Passenger(TimeStampModel):
    firstName = models.CharField(max_length=20)
    lastName  = models.CharField(max_length=20)
    email     = models.CharField(max_length=20)
    phone     = models.CharField(max_length=20)


class Reservation(TimeStampModel):
    flight    = models.ForeignKey('Flight', on_delete=models.CASCADE)
    passenger = models.OneToOneField('Passenger', on_delete=models.CASCADE)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)