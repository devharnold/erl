from rest_framework.views import APIView
from mod.models import Post
from mod.serializers import PostSerializer
from mod.permissions.permissions import IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
#from django.views.decorators.vary import vary_on_cookie, vary_on_headers

class PostList(APIView):
    """Handle operations of Posts at a List level
       retrieved posts will be cached
    Params:
        permission_classes: permission methods allowed in this program
        get: Retrieves a list of posts
        post: Post a new Post
    """
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # Add cache decorator
    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, data=request.data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #def get(self, request, format=None):
    #    posts = Post.objects.all()
    #    serializer = PostSerializer(posts, data=request.data, many=True)
    #    return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostDetail(APIView):
    """Handles operation of posts at individual level
    Params:
        permission_classes: permission methods allowed in the program
        get_objects: retrieve a post by its primary key
        put: update a specific post
        delete: deletes a specific post
    """
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_objects(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)