from django.shortcuts import render, redirect
from django.http import HttpResponse

from images_repo.models import Image
from .forms import ImageForm


def home(request):
    return render(request, 'images_repo/home.html', {})

def add_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            image_object = form.instance
            return render(request, 'images_repo/add_image.html', 
                            {'form': form, 'image_object': image_object})
    else:
        form = ImageForm()
    return render(request, 'images_repo/add_image.html', {'form' : form})


def all_images(request):
    image_list = Image.objects.all()
    return render(request, 'images_repo/gallery.html', {'image_list': image_list})

def delete_image(request):
    pass


# Create your views here.

