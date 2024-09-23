from django.db import models
from utils.utils import photo_upload_to


class Headline(models.Model):
    name = models.CharField(max_length=200, default="headlines_pics")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo_main = models.ImageField(upload_to=photo_upload_to, blank=True, null=True)
    def __str__(self):
        return self.title
