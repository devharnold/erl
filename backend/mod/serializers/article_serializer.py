from rest_framework import serializers
from mod.models import Article


class ArticleSerializer(serializers.Serializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

    def validate_title(self, value: str) -> str:
        if not value.strip():
            raise serializers.ValidateError("Title missing!")
        return value