from django.contrib import admin
from .models import School

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id','name','city','province')
    list_display_links = ('id', 'name')
    search_fields = ('name','city','province')
    list_per_page = 25

admin.site.register(School,SchoolAdmin)