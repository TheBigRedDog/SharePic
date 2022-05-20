from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_image', views.add_image, name='add-image'),
    path('gallery', views.all_images, name='gallery'),
    path('delete_image/<image_id>', views.delete_image, name='delete_image'),

]