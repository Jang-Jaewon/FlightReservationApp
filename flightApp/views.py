from rest_framework             import viewsets
from rest_framework             import status
from rest_framework.response    import Response
from rest_framework.decorators  import api_view
from rest_framework             import filters
from rest_framework.permissions import IsAuthenticated

from .models      import Flight, Passenger, Reservation
from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset           = Flight.objects.all()
    serializer_class   = FlightSerializer
    filter_backends    = [filters.SearchFilter]
    search_fields      = ['departureCity', 'arriveCity', 'dateOfDeparture']
    permission_classes = (IsAuthenticated, )


class PassengerViewSet(viewsets.ModelViewSet):
    queryset         = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = (IsAuthenticated, )


class ReservationViewSet(viewsets.ModelViewSet):
    queryset         = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated, )


@api_view(['POST'])
def find_flights(request):
    departureCity   = request.data['departureCity']
    arriveCity      = request.data['arriveCity']
    dateOfDeparture = request.data['dateOfDeparture']
    
    flights   = Flight.objects.filter(departureCity=departureCity, arriveCity=arriveCity, dateOfDeparture=dateOfDeparture)
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['flightId'])

    passenger           = Passenger()
    passenger.firstName = request.data['firstName']
    passenger.lastName  = request.data['lastName']
    passenger.email     = request.data['email']
    passenger.phone     = request.data['phone']
    passenger.save()

    reservation           = Reservation()
    reservation.flight    = flight
    reservation.passenger = passenger
    reservation.save()

    return Response(status=status.HTTP_201_CREATED)


