from django.urls import path
from .views import get_contact

urlpatterns = [
    path('get/', get_contact),
]