from rest_framework.viewsets import ModelViewSet
from .models import MaintenanceRequest
from .serializers import MaintenanceRequestSerializer

class MaintenanceViewSet(ModelViewSet):
    queryset = MaintenanceRequest.objects.all() # pylint: disable=no-member
    serializer_class = MaintenanceRequestSerializer
