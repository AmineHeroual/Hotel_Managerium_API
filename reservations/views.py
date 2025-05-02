from rest_framework.viewsets import ModelViewSet
from .models import Reservation
from .serializers import ReservationSerializer

class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all() # pylint: disable=no-member
    serializer_class = ReservationSerializer
