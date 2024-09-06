from django.db import models
from PIL import Image



class Post(models.Model):
    title = models.CharField(max_length=225)
    description = models.CharField(max_length=200)
    image_url = models.ImageField(upload_to="posts", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        #check if image exists
        if self.image:
            img = Image.open(self.image.path)

            max_size = (800, 800)
            if img.height > max_size[0] or img.width > max_size[1]:
                img.thumbnail(max_size)
                img.save(self.image.path)

    def __str__(self):
        return self.title