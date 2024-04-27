# urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import register,home

urlpatterns = [
    # Your existing URL patterns
    path('register/', register, name='register'),
    path('home/', home, name='home'),
]