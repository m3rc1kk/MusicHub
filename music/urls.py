from django.urls import path
from .views import *

urlpatterns = [
    
    path('main/', main_page, name = 'main'),
    path('uploadmusic/', upload_music, name = 'upload-music' ),
    path('home/', ListMusicView.as_view(), name = 'home')
]
