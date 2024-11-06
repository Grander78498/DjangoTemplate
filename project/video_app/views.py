import json
import time

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from .models import FileUpload
from .forms import UploadFileForm
from . import utils


def root_page(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('login-page'))
    return redirect(reverse_lazy('main-page'))


def main_page(request):
    if request.method == 'POST':
        print(request.POST, request.FILES)
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = FileUpload.objects.create(file=request.FILES['file'])
            file_path = file.file.path
            client = utils.get_client()
            result = utils.predict_model(file_path, client)
            print(result)
            return HttpResponse('Fine')
    else:
        form = UploadFileForm()
    return render(request, 'video_app/index.html', {'form': form})
