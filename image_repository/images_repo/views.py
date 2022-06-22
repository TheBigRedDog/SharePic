from django.shortcuts import render, redirect
from django.contrib import messages
from urllib3 import HTTPResponse
from images_repo.models import Image
from .forms import ImageForm
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .functions import *
def home(request):
    return render(request, 'images_repo/home.html', {})

@login_required(login_url='/members/login_user')
def add_image(request):
    

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            
            # image_is_nsfw = check_image_nsfw(form=form)
            # if image_is_nsfw:
            #     messages.error(request, ('All image uploads must be of appropriate content.'))
            #     form = ImageForm()
            #     return render(request, 'images_repo/add_image.html', {'form': form})
            
            form.save(commit=False)
            image_object = form.instance
           
            image_object.owner = request.user
            image_object.save()
            return render(request, 'images_repo/add_image.html', 
                            {'form': form, 'image_object': image_object})

        else:
            messages.error(request, ('There was an error with your form'))
    else:
        form = ImageForm()
    return render(request, 'images_repo/add_image.html', {'form' : form})

def all_images(request):
    if request.user.is_authenticated:
        image_list = Image.objects.filter(Q(public=True) | Q(owner=request.user))
    else:
        image_list = Image.objects.filter(Q(public=True))

    return render(request, 'images_repo/gallery.html', {'image_list': image_list})

# TODO: IMPLEMENT DELETING image from file location w/django-cleanup
def delete_image(request, image_id):
    if request.user.is_authenticated:
        image = Image.objects.get(pk=image_id)
        if request.user == image.owner:
            image.delete()
            messages.success(request, (f'Image {image.title} has been deleted'))
        else:
            messages.error(request, ('You can only delete your own images!'))
        return redirect('gallery')
    else:
        messages.error(request, ('You must be logged in to delete images'))
        return redirect('gallery')