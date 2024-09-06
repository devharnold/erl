from rest_framework.views import APIView
from mod.models import Blog
from mod.serializers import  BlogSerializer
from mod.permissions.permissions import IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class BlogList(APIView):
    """Retrieves a list of blogs
    Params:
        Permission_classes: Permission methods allowed in the class
        get: Retrieve the list of blogs
        post: Post a new blog
    """
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get(self, request, format=None):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, data=request.data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BlogDetail(APIView):
    """Handle operation on individual Blog instances
    Params:
        permission_classes: permission_methods used in this program
        get_objects: Retrieve a specific blog by its primary key
        get: Retrieve a specific blog by its primary key
        put: Update a specific blog by its primary key
        delete: Deletes a specific blog by its primary key
    """
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_objects(self, pk):
        """Retrieve a blog by its primary key"""
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DeoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        """Retrieve a blog by its primary key"""
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        """Update a specific blog by its pk"""
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        """Deletes a blog by its pk"""
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)