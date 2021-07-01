from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import PictureForm

def display_pictures(request):
    '''
    Show all pictures
    '''
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Picture has been saved')

        else:
            messages.info(request, 'Invalid form. Picture has not been saved')

        return redirect(reverse('pictures:display_pictures'))

    else:
        form = PictureForm()

    context = {
        'picture_form': form
    }
    template = 'pictures/pictures.html'
    return render(request, template, context)
