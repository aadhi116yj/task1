from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('details/', views.details, name="details"),
    path('replace/<int:id>/',views.replace, name="replace"),
    path('dell/<int:id>/',views.dell, name="dell"),
]