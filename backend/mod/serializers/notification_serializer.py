from rest_framework import serializers
from mod.models import Notification

class NotificationSerializer(serializers.Serializer):
    """Serializer for the { Notification }object model"""
    class Meta:
        model = Notification
        fields = ['id', 'user', 'title', 'message', 'read', 'created_at']
        read_only_fields = ['user', 'created_at']

    def validate_title(self, value: str) -> str:
        if not value.strip():
            raise serializers.ValidateError("Title of notification is empty")
        return value
    