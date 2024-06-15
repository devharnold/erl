from rest_framework import viewsets
from mod.models import Blog
from mod.serializers import  BlogSerializer
from mod.permissions.permissions import IsAdminOrReadOnly

class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for { Blog }object model
    """
    queryset = Blog.objects.all().select_related('module')
    serializer_class = BlogSerializer
    permission_classes = [IsAdminOrReadOnly]