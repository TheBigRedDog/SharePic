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

def success(request):
    return HttpResponse('upload successful')

def all_images(request):
    images_list = Image.objects.all()
    return render(request, 'images_repo/image_gallery.html', {'image_list': image_list})

# Create your views here.

