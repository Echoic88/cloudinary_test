from django.urls import path
from .apps import PicturesConfig
from . import views

app_name = PicturesConfig.name
urlpatterns = [
    path('', views.display_pictures, name='display_pictures'),
]