from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path('register/', UserRegisterView, name = 'register'),
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    
    path('detail/<int:pk>', DetailUser.as_view(), name = 'detail'),
    path('detail/<int:pk>/album/', DetailUserAlbum.as_view(), name = 'detail-album'),

    
    
    
   
    
]
