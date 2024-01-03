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
    path('create_playlist/', create_playlist, name = 'create-playlist'),
    path('home/playlist/', PlayListView.as_view() , name = 'playlist'),
    path('home/playlist/detail/<int:pk>/', PlayListDetailView, name = 'playlist-detail'),
    path('delete/playlist/<int:pk>/', DeletePlayListView.as_view(), name = 'delete-playlist'),
]
