from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from mod.models import Notification
from mod.serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    """
    API view to retrieve list of notifications for the authenticated user.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)


class NotificationUpdateView(generics.UpdateAPIView):
    """
    API view to update a notification (mark as read).
    """
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)