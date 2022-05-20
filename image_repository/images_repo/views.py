from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
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

# TODO: IMPLEMENT DELETING IMAGES
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

 
# TODO: IMPLEMENT ADDING MULTIPLE IMAGES AS ALBUM
# def add_album(request):
#     if request.method ==

# TODO: IMPLEMENT DELETING ALBUMS


# Create your views here.

