#from django.conf.urls import url
from .views import FileView, FileAllView
from django.urls import  path

urlpatterns = [
    path('upload_file/', FileView.as_view(),name='file-upload'),
    path('all_file_data/',FileAllView.as_view(), name='all-file'),
]