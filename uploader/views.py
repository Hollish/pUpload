from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.files import File
from django.shortcuts import get_object_or_404, render
import os
from .models import UserFile
from .forms import UploadFileForm

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/d/')
    else:
        form = UploadFileForm()
    return render(request, 'uploader/index.html', {'form': form})

def detail(request, fileID):  
    targetFile = get_object_or_404(UserFile, upload = fileID)
    context = {'targetFile': targetFile}
    return render(request, 'uploader/detail.html', context)

def download(request, fileID):    
    targetFile = get_object_or_404(UserFile, upload = fileID)
    fileData = File(open(settings.MEDIA_ROOT+targetFile.upload.url, 'r'))
    response = HttpResponse(fileData, content_type='application/force-download')

    response['Content-Disposition'] = 'attachment; filename=%s' % targetFile.upload.name
    return response