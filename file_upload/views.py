from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, View
from django.http import HttpResponse
from .models import UploadedFile
from django.urls import reverse_lazy

# Create your views here.

class FileListView(ListView):
    model = UploadedFile
    template_name = 'file_upload/file_list.html'
    context_object_name = 'files'

class FileUploadView(CreateView):
    model = UploadedFile
    template_name = 'file_upload/file_upload.html'
    fields = ['file']
    success_url = reverse_lazy('file-list')

class FileDownloadView(View):
    def get(self, request, pk):
        file_obj = get_object_or_404(UploadedFile, pk=pk)
        file_contents = file_obj.get_file_contents()
        
        if file_contents is None:
            return HttpResponse("File not found", status=404)
            
        response = HttpResponse(file_contents)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = f'attachment; filename="{file_obj}"'
        return response
