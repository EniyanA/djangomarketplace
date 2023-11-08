from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name= models.CharField(max_length=225)

    class Meta:
        ordering=('name',)
        verbose_name_plural= 'Categories'

    def __str__(self):
        return self.name
    

class Item(models.Model):
    category=models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE )
    name= models.CharField(max_length=225)
    description= models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    price = models.FloatField()
    is_sold = models.BooleanField()
    created_by = models.CharField(max_length=50)
    Created_at = models.DateTimeField(auto_now_add=True)
    experience = models.CharField(max_length=225, default='not provided')
    otherprojects = models.CharField(max_length=225, default='not provided')

    def __str__(self):
        return self.name
