from rest_framework import serializers
from mod.models import Blog

class BlogSerializer(serializers.Serializer):
    """"Serializer class for { Blog }object model"""
    class Meta:
        model = Blog
        fields = '__all__'

    def validate_title(self, value: str) -> str:
        if not value.strip():
            raise serializers.ValidationError("Title is blank")
        return value