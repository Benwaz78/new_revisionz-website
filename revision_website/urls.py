from django.contrib import admin
from django.urls import path, include
from blog_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-page/', views.about, name='about'),
    path('service-page/', views.services, name='services'),
    path('tinymce/', include('tinymce.urls')),
    path('site-admin/', admin.site.urls),
]
