from rest_framework import serializers
from mod.models import Post

class PostSerializer(serializers.Serializer):
    """Serializer for the { Post }object model"""
    class Meta:
        model = Post
        fields = ['id', 'user', 'title']
        read_only_fields = ['user', 'created_at']

    def validate_title(self, value: str) -> str:
        if not value.strip():
            raise serializers.ValidateError("Title missing!")
        return value