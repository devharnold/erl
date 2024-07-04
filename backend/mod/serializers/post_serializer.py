from rest_framework import serializers
from mod.models import Post
from django.core.exceptions import ValidationError

from mod.validators import validate_image_size

class PostSerializer(serializers.Serializer):
    """Serializer for the { Post }object model"""
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'image', 'description', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']

    def validate_title(self, value: str) -> str:
        if not value.strip():
            raise serializers.ValidateError("Title missing!")
        return value
    
    def validate_image(self, value):
        try:
            validate_image_size(self)
        except ValidationError as e:
            raise serializers.ValidationError(e.message)
        return value