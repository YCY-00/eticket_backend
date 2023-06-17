from rest_framework import serializers
from .models import TicketModel

class TicketModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketModel
        fields = '__all__'
