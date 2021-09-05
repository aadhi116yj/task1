from django.urls import path
from .import views

urlpatterns = [
    path('table/', views.table, name="table"),
    path('table2/', views.table2, name="table2"),
    path('task/<int:num>/', views.task, name="task"),
    path('bootonline/', views.bootonline, name="bootonline"),
    path('bootoffline/', views.bootoffline, name="bootoffline"),
]