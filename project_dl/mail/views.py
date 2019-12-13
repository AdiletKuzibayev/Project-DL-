from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

# Imaginary function to handle an uploaded file.
<<<<<<< HEAD

=======
from .models import Homework
>>>>>>> parent of 34c64c1... asd
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
<<<<<<< HEAD
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
=======
            form.save(commit=False)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def uploaded_file(request):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        form = Homework(work_file=request.FILES['work_file'])
        form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = UploadFileForm()
    return render(request, 'homeworks.html', {'form': form})
>>>>>>> parent of 34c64c1... asd
