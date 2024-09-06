from rest_framework import serializers
from django.contrib.auth.models import User

class EditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ['username', 'first_name', 'last_name', 'email']
        read_only_fields = ['username']