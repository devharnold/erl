from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from mod.serializers import EditProfileSerializer
from django.contrib.auth.models import User


class EditProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user # get user's data
        serializer = EditProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request):
        #update user's profile
        user = request.user
        serializer = EditProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)