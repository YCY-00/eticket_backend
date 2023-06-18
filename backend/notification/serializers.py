from rest_framework import serializers

from backend.notification.models import NotificationModel


class NotificationSerializer(serializers.Serializer):
    class Meta:
        model = NotificationModel
        fields = "__all__"

        extra_kwargs = {
            "url": {"view_name": "api:notification-detail", "lookup_field": "id"},
        }

    title = serializers.CharField(max_length=1000)
    message = serializers.CharField(max_length=1000)
    updated_at = serializers.DateTimeField()
    created_at = serializers.DateTimeField()
    user = serializers.CharField(max_length=1000)
    id = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        return NotificationModel.objects.create(**validated_data)

    def update(self, instance: NotificationModel, validated_data: dict):
        instance.title = validated_data.get("title", instance.title)
        instance.message = validated_data.get("message", instance.message)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)
        instance.created_at = validated_data.get("created_at", instance.created_at)
        instance.user = validated_data.get("user", instance.user)
        instance.save()
        return instance
