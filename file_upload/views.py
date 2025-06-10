from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, View
from django.http import HttpResponse, FileResponse
from .models import UploadedFile
from django.urls import reverse_lazy
import mimetypes
import os

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
        
        try:
            # Get the file directly from the storage backend
            file = file_obj.file
            file_extension = os.path.splitext(file.name)[1].lower()
            content_type, _ = mimetypes.guess_type(file.name)
            
            if content_type is None:
                content_type = 'application/octet-stream'
            
            # Create a FileResponse with the file
            response = FileResponse(file, content_type=content_type)
            
            # Always force download for all file types
            response['Content-Disposition'] = f'attachment; filename="{file_obj}"'
            
            return response
            
        except Exception as e:
            print(f"Error downloading file: {e}")
            return HttpResponse("Error downloading file", status=500)
