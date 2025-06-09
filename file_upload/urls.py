from django.urls import path
from . import views

urlpatterns = [
    path('', views.FileListView.as_view(), name='file-list'),
    path('upload/', views.FileUploadView.as_view(), name='file-upload'),
    path('download/<int:pk>/', views.FileDownloadView.as_view(), name='file-download'),
] 