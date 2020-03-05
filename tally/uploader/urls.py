from django.urls import path

from . import views


urlpatterns = [
   # path('file_uploader_index', views.file_uploader_index, name='file_uploader_index'),
    path('upload', views.upload_file_view, name='file_upload_1'),
    path( 'uploadToS3' , views.upload_file_to_s3 , name = 'file_upload' ),
    path( 'success' , views.success_page , name = 'success' ),
    path( 'all_files' , views.all_files , name = 'success' ),
]


