from django.urls import path
from .import views

urlpatterns = [
    path('demo/', views.demo, name="demo"),
    path('show/', views.show, name="show"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
]