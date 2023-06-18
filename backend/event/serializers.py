from rest_framework import serializers

from backend.event.models import EventModel


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]

        depth = 1
