from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from testapp.models import *
# Register your models here.

class PublisherAdmin(admin.ModelAdmin):
    list_display=['name','address','city','country','wbsite']
admin.site.register(Publisher,PublisherAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','emails']
admin.site.register(Author,AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_dispaly=['title','author','publisher']
admin.site.register(Book,BookAdmin)