from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status

class SearchUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.query_params.get('q', '')
        if not query:
            return Response({"error": "No search query provided!"}, status=status.HTTP_400_BAD_REQUEST)
        
        users = User.objects.filter(
            username_icontains=query
        ) | User.objects.filter(
            firstName_icontains=query
        )

        user_data = [{"username": user.username, "email": user.email} for user in users]
        return Response({"users": user_data}, status=status.HTTP_200_OK)