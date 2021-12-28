from django.contrib import admin

# Register your models here.
from testapp.models import Page

class PageAdmin(admin.ModelAdmin):
    list_display=['user','page_name','page_cat','page_publish_date']
    
admin.site.register(Page,PageAdmin)
