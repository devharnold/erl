from rest_framework import viewsets
from mod.models import Post
from mod.serializers import  PostSerializer
from mod.permissions.permissions import IsAdminOrReadOnly

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for { Post }object model
    """
    queryset = Post.objects.all().select_related('module')
    serializer_class = PostSerializer
    permission_classes = [IsAdminOrReadOnly]