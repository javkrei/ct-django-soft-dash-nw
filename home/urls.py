from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('audio/upload/', views.audio_upload, name='audio_upload'),
]
