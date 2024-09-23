from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('blogs/<slug:slug>/', views.blogs),
]
