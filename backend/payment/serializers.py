from rest_framework import serializers

from backend.payment.models import PaymentModel


class PaymentSerializer(serializers.Serializer):
    class Meta:
        model = PaymentModel
        fields = "__all__"

        extra_kwargs = {
            "url": {"view_name": "api:payment-detail", "lookup_field": "id"},
        }

    ticket = serializers.CharField(max_length=1000)
    updated_at = serializers.DateTimeField()
    created_at = serializers.DateTimeField()
    customer = serializers.CharField(max_length=1000)
    is_refunded = serializers.BooleanField()
    id = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        return PaymentModel.objects.create(**validated_data)

    def update(self, instance: PaymentModel, validated_data: dict):
        instance.ticket = validated_data.get("ticket", instance.ticket)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)
        instance.created_at = validated_data.get("created_at", instance.created_at)
        instance.customer = validated_data.get("customer", instance.customer)
        instance.is_refunded = validated_data.get("is_refunded", instance.is_refunded)
        instance.save()
        return instance
