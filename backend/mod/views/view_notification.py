from rest_framework import generics, permissions
from mod.models import Notification
from mod.serializers import NotificationSerializer
from mod.permissions.permissions import IsAdminOrReadOnly

class NotificationListView(generics.ListAPIView):
    """
    API view to retrieve list of notifications for the authenticated user.
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)


class NotificationUpdateView(generics.UpdateAPIView):
    """
    API view to update a notification (mark as read).
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notification.objects.all()

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)