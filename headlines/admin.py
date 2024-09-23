from django.contrib import admin
from .models import Headline

class HeadlineAdmin(admin.ModelAdmin):
    list_display = ('id','title','description')

admin.site.register(Headline, HeadlineAdmin)