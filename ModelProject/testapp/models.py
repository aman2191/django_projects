from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=50)
    wbsite=models.URLField()
    
    def __str__(self):
        return self.name
    
class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    emails=models.EmailField()
    
    def __str__(self):
        return self.first_name
    
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ManyToManyField(Author)
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title