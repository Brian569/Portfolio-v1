from django.urls import path
from .views import (
    home, upload,
    more
)

urlpatterns = [
    path('', home, name = 'home'),
    path('upload/', upload, name = 'upload'),
    path('more/', more, name = 'more')
]