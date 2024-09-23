from django.db import models
from django.contrib.postgres.fields import IntegerRangeField
from utils.utils import photo_upload_to
from schools.models import School
from headlines.models import Headline

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class AccommodationOption(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.name} - ${self.price}"

class Listing(models.Model):
    school = models.ForeignKey(School, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_mvp = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    hourperweek = models.IntegerField()
    studentnumber = models.IntegerField()
    agerange = IntegerRangeField()
    is_published = models.BooleanField(default=True)
    #added
    age_limit = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    headline = models.ManyToManyField(Headline, related_name='listings', blank=True)
    accommodation = models.BooleanField(default=True)
    accommodation_options = models.ManyToManyField(AccommodationOption, null=True)
    recreation = models.TextField(blank=True)
    def __str__(self):
        return self.title