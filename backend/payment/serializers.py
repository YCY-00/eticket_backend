from rest_framework import serializers

from backend.payment.models import PaymentModel
from backend.ticket.serializers import TicketSerializer


class PaymentSerializer(serializers.ModelSerializer):
    ticket = TicketSerializer()

    class Meta:
        model = PaymentModel
        fields = "__all__"
        extra_kwargs = {
            "url": {"view_name": "api:payment-detail", "lookup_field": "id"},
        }

    def create(self, validated_data):
        return PaymentModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)
        instance.is_refunded = validated_data.get("is_refunded", instance.is_refunded)
        instance.save()
        return instance
