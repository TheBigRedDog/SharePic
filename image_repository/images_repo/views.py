from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm

def home(request):
    return render(request, 'images_repo/home.html', {})

def add_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'images_repo/add_image.html', {'form' : form})

def success(request):
    return HttpResponse('upload successful')


# Create your views here.

