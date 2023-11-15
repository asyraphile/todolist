from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tasks', views.TodoViewSet, basename="task")

urlpatterns = [
    path('hello_world/', views.hello_world, name="Hello World"),
] + router.urls
