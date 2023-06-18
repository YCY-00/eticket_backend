# class TicketModel(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     event = models.ForeignKey('event.EventModel', on_delete=models.CASCADE, related_name='tickets')
#     price = models.FloatField()
#     updated_at = models.DateTimeField(auto_now=True)
#     created_at = models.DateTimeField(auto_now_add=True)
from rest_framework import serializers
from .models import TicketModel


class TicketSerializer(serializers.Serializer):
    class Meta:
        model = TicketModel
        fields = "__all__"
        extra_kwargs = {"url": {"view_name": "api:ticket-detail", "lookup_field": "id"}}

    event = serializers.CharField(max_length=1000)
    price = serializers.FloatField()
    updated_at = serializers.DateTimeField()
    created_at = serializers.DateTimeField()
    id = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        return TicketModel.objects.create(**validated_data)

    def update(self, instance: TicketModel, validated_data: dict):
        instance.event = validated_data.get("event", instance.event)
        instance.price = validated_data.get("price", instance.price)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)
        instance.created_at = validated_data.get("created_at", instance.created_at)
        instance.save()
        return instance
