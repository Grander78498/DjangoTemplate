import json
import time
import base64

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from .models import FileUpload
from .forms import UploadFileForm
from . import utils
from . import tasks


def root_page(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('login-page'))
    return redirect(reverse_lazy('main-page'))


def main_page(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file'].read()
            byte = base64.b64encode(file)

            data = {'file': byte.decode('utf-8'),
                    'name': request.FILES['file'].name}

            tasks.task_upload_file.delay(data=data)
            return HttpResponse('Fine')
    else:
        form = UploadFileForm()
    return render(request, 'video_app/index.html', {'form': form})
