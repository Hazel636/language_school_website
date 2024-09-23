from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone','wechat_account','Contact_date')
    list_display_links = ('id','name')
    search_fields = ('name', 'email', 'listing','school')
    list_per_page = 25
    
admin.site.register(Contact,ContactAdmin)