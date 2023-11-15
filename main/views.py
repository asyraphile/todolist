from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task
from rest_framework.response import Response

# Create your views here.

def hello_world(request):
    return JsonResponse({"hello": "world"})

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    def get_queryset(self):
        queryset = Task.objects.all()
        return queryset
    