from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage
import os
import boto3
from django.conf import settings

# Create your models here.

class UploadedFile(models.Model):
    file = models.FileField(storage=S3Boto3Storage())
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return os.path.basename(self.file.name)

    def get_file_contents(self):
        """Retrieve file contents from S3"""
        try:
            # Get the file directly from the storage backend
            return self.file.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            return None

    def get_file_url(self):
        """Get the full S3 URL for the file"""
        return self.file.url
