from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from mod.models import Article
from mod.serializers import ArticleSerializer
from mod.permissions.permissions import IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class ArticleList(APIView):
    """Implements functionality to retrieve a list of articles
    Params:
        permission_classes: Permission methods implemented
        get: Retrieve a list of articles
        post: Post a new article
    """
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get(self, request, format=None):
        """Gets a list of articles"""
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, data=request.data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        """Post a new article"""
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ArticleDetail(APIView):
    """Handle operation on individual article instances
    Params:
        get_object: Retrieve the article by the primary key
        get: retrieve a single article by its primary key
        put: Updates a single article identified by its primary key
        delete: deletes an article identified by its specific pk
    """
    permission_classes = [IsAuthenticated]

    def get_objects(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        """Retrieve a single article by its primary key"""
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        """Update a specific artiiiicle according to its primary key"""
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, pk, format=None):
        """Delete a specific article"""
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)