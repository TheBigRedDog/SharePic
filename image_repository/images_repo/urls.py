from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_image', views.add_image, name='add-image'),
    path('gallery', views.all_images, name='gallery'),
]