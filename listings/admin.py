from django.contrib import admin
from .models import Listing, AccommodationOption, Category

class AccommodationOptionAdmin(admin.ModelAdmin):
    list_display = ('id','name','price')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','school','price','is_published')
    list_display_links = ('id', 'title')
    list_filter = ('school',)
    list_editable = ('is_published',)
    search_fields = ('title','school__name')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)
admin.site.register(AccommodationOption, AccommodationOptionAdmin)
admin.site.register(Category, CategoryAdmin)