from django.urls import path
from . import views

urlpatterns = [
    path('list_all/', views.get_all, name="List All To Do"),
    path('add_item/', views.add_item, name="Add Item"),
    path('delete_item/', views.delete_item, name="Delete Item"),
    path('mark_completed/<int:task_id>/', views.mark_completed, name="Mark Completed"),
]
