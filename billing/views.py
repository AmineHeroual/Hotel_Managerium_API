from rest_framework.viewsets import ModelViewSet
from .models import Invoice
from .serializers import InvoiceSerializer

class BillViewSet(ModelViewSet):
    queryset = Invoice.objects.all() # pylint: disable=no-member
    serializer_class = InvoiceSerializer
