from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce import models as tinymce_models
from django.conf import settings



class CustomUser(AbstractUser):
    pass


class AboutUs(models.Model):
    title = models.CharField(max_length=120)
    profile = models.ImageField(blank=True, null=True, upload_to='uploadds/')
    content = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name_plural = 'About Us'


class Category(models.Model):
    cat_name = models.CharField(max_length=100, unique=True, verbose_name='Category Name', blank=True, null=True, )
    slug = models.SlugField(unique=True)
    cat_desc = tinymce_models.HTMLField('Category', blank=True, null=True)

    def __str__(self):
        return self.cat_name
    
    class Meta():
        verbose_name_plural = 'Category'


class Post(models.Model):
    pst_title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, max_length=250)
    pst_image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    content = tinymce_models.HTMLField('Content', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.pst_title

    
    def img_url(self):
        if self.pst_image:
            return self.pst_image.url

class Comment(models.Model):
    name = models.CharField(max_length=80,verbose_name= 'Name')
    email = models.EmailField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE,related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    class Meta():
        verbose_name_plural = ' Comments'

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)