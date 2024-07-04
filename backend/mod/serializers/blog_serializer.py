from rest_framework import serializers
from rest_framework.validators import UniqueForYearValidator
from django.core.exceptions import ValidationError
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
    
    def validate_empty_values(self, value: str) -> str:
        if not value.strip():
            raise serializers.ValidationError("Empty values are not allowed")
        return value
    
    def validate_blog(self, value: str) -> str:
        if not value.strip():
            raise serializers.ValidationError("Blog is empty")
        return value
    
class BlogWithYear(serializers.Serializer):
    """Blogs have a slug thats unique for the current year"""
    class Meta:
        validators = [
            UniqueForYearValidator(
                queryset=Blog.objects.all(),
                field='slug',
                date_field='published'
            )
        ]