from rest_framework import serializers
from .models import TicketModel

class TicketModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketModel
        fields = '__all__'
        read_only_fields = ["id", "created_at", "updated_at"]
