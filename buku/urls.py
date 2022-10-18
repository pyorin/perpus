from django.urls import path
from . import views

app_name = 'buku'
urlpatterns = [
    path('', views.index),
    path('delete/<int:buku_id>', views.delete, name="delete"),
    path('edit/<int:buku_id>', views.edit, name="edit")
]