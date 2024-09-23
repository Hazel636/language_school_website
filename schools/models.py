from django.db import models
from utils.utils import photo_upload_to


class School(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_mvp = models.BooleanField(default=False)
    photo_main = models.ImageField(upload_to=photo_upload_to, blank=True, null=True)
    photo_1 = models.ImageField(upload_to=photo_upload_to, blank=True, null=True)
    photo_2 = models.ImageField(upload_to=photo_upload_to, blank=True, null=True)
    photo_3 = models.ImageField(upload_to=photo_upload_to, blank=True, null=True)
    photo_4 = models.ImageField(upload_to=photo_upload_to, blank=True, null=True)
    photo_5 = models.ImageField(upload_to=photo_upload_to, blank=True, null=True)
    photo_6 = models.ImageField(upload_to=photo_upload_to, blank=True, null=True)
    photo_7 = models.ImageField(upload_to=photo_upload_to, blank=True, null=True)
    photo_8 = models.ImageField(upload_to=photo_upload_to, blank=True, null=True)
    photo_9 = models.ImageField(upload_to=photo_upload_to, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    #added
    note = models.TextField(blank=True)
    def __str__(self):
        return self.name