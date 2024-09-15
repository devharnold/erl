from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from mod.serializers import LoginSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.is_validated_data['username']
            password = serializer.is_validates_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({"message": "Login Successful"}, status=status.HTTP_200_OK)
            return Response({"message": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
