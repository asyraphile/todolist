from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        #fields = ['user', 'title', 'description', 'completed']
        fields = '__all__'