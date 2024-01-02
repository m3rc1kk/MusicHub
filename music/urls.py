from django.urls import path
from .views import *

urlpatterns = [
    
    path('main/', main_page, name = 'main'),
    path('uploadmusic/', upload_music, name = 'upload-music' ),
    path('home/', ListMusicView.as_view(), name = 'home'),
    path('delete/<int:pk>/', DeleteMusicView.as_view(), name = 'delete'),
    path('create_album/', create_album, name = 'create-album'),
    path('home/albums/', AlbumMusicView.as_view() , name = 'album-list'),
    path('home/albums/detail/<int:pk>/', AlbumDetailView, name = 'album-detail'),
    path('delete/album/<int:pk>/', DeleteAlbumView.as_view(), name = 'delete-album'),
]
