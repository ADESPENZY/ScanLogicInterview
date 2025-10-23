from django.urls import path
from . import views

urlpatterns = [
    path('getProfile/', views.get_profile),
    path('saveProfile/', views.save_profile),
]
