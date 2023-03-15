from django.contrib import admin
from blog_app.models import *
from django.utils.html import format_html, strip_tags



@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):


    list_display = [
        'username',
        'first_name',
        'last_name',
        'email',
        ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = [
        'cat_name',
        ]
    
    prepopulated_fields = {'slug': ('cat_name',)}


@admin.register(Post) 
class PostAdmin(admin.ModelAdmin):

    def get_thumbnail_img(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.img_url()))
    
    def get_content(self,obj):
        return strip_tags(obj.content)


    list_display = [
        
        'pst_title',
        'get_thumbnail_img',
        'get_content',
        'created',
        'modified', 
        
        ]
    prepopulated_fields = {'slug': ('pst_title',)}


@admin.register(AboutUs) 
class AboutUsAdmin(admin.ModelAdmin):

    def get_thumbnail_img(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.img_url()))


    list_display = [
        'title',
        'get_thumbnail_img',
        'content',
        ]
    
@admin.register(ServiceModel) 
class ServiceModelAdmin(admin.ModelAdmin):

    def get_content(self,obj):
        return strip_tags(obj.content)


    list_display = [
        'title',
        'get_content',
        ]


@admin.register(Comment) 
class CommentAdmin(admin.ModelAdmin):

    list_display = [
        
        'name',
        'email',
        'created_on',
        
        ]