from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(MusicModel)
class MusicAdmin(admin.ModelAdmin):
    pass

@admin.register(AlbumModel)
class AlbumAdmin(admin.ModelAdmin):
    pass
