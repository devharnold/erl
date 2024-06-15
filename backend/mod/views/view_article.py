from rest_framework import viewsets
from mod.models import Article
from mod.serializers import ArticleSerializer
from mod.permissions.permissions import IsAdminOrReadOnly

class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for { Article }object model
    """
    queryset = Article.objects.all().selected_related('module')
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminOrReadOnly]