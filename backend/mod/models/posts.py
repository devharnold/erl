from django.db import models
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=225)
    description = models.CharField(max_length=200)
    image_url = models.ImageField(upload_to="posts", blank=True, null=True)
    content = models.TextField(default="Default content", null=True, blank=True)  # Set a default value here
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Check if image exists
        if self.image_url:
            img = Image.open(self.image_url.path)
            max_size = (800, 800)
            if img.height > max_size[0] or img.width > max_size[1]:
                img.thumbnail(max_size)
                img.save(self.image_url.path)

    def __str__(self):
        return self.title
