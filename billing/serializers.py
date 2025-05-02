from rest_framework import serializers
from .models import Invoice
from users.models import User

class InvoiceSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Invoice
        fields ='__all__'
