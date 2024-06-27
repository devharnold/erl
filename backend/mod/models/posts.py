from django.db import models
from django.contrib.auth.models import User
from imagefield.fields import ImageField
from imagefield.processing import register

class ImageModel(models.Model):
    """Implementation of the ImageField object model"""
    image = ImageField(
        upload_to="images",
        formats = {
            "thumb": ["default", ("crop", (300, 300))],
            "desktop": ["default", ("thumbnail", (300, 225))],
        },
        auto_add_fields=True,
    )

class Post(models.Model):
    """
    Posts: can be pictures and videos
    Attr:
        title(str): The post's title
        post_type(str): The type of post shared by the user(
        video, picutre)
    """

    POST_TYPES = ('picture', 'Picture')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='post/%Y/%m/%d/', null=True, max_length=225)
    description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'mod'
        ordering = ['-created_at']