from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Page(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    page_name=models.CharField(max_length=100)
    page_cat=models.CharField(max_length=100)
    page_publish_date=models.DateTimeField()
    
    def __str__(self):
        return self.page_name
    
    
