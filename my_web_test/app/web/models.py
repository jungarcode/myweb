from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 100, null = False,blank = False)
    state = models.BooleanField(default = True)
    created = models.DateTimeField( auto_now_add=True)
    update= models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['created']


    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.CharField(max_length = 100, blank = True, null = True)
    description = models.CharField(max_length = 300, blank = False, null = False)
    # content =models.CharField(max_length = 100000)
    content = CKEditor5Field(config_name='extends')
    published =models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to= "blog", null= True , blank= True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    state = models.BooleanField(default = True)
    categories = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created']

    def __str__(self):
        return self.title