from django.db import models
from datetime import datetime

class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100,blank=True)
    wechat_account = models.CharField(max_length=100,blank=True)
    message = models.TextField(blank=True)
    Contact_date = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.name