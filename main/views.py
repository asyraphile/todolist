from django.contrib.auth.models import User
from rest_framework import status
from .serializers import TaskSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Task
from rest_framework.response import Response

# Create your views here.

#List All To do
@api_view(['GET'])
def get_all(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        serialized = TaskSerializer(tasks, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    else:
        message = {
            'detail': 'Method is not allowed.'
        }
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
#Add a To do
@api_view(['POST'])
def add_item(request):
    user = request.query_params.get('user_id')
    title = request.query_params.get('title')
    if user is None or title is None:
        return Response({'detail': 'user_id or title is required in the parameter.'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "POST":
        user = User.objects.get(id=user)
        if user:
            try:
                Task.objects.create(user=user, title=title)
                return Response({'detail': 'Task have been created successfully.'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'detail': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': f'User ID does not exist in the system'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        message = {
            'detail': 'Method is not allowed.'
        }
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
#Delete a to do
@api_view(['DELETE'])
def delete_item(request):
    task = request.query_params.get('task_id')
    if task is None:
        return Response({'detail': 'task_id is required in the parameter.'}, status=status.HTTP_400_BAD_REQUEST)
    Task.objects.filter(id=task).delete()
    return Response({'detail': 'Task has successfully been deleted.'}, status=status.HTTP_200_OK)

@api_view(['PUT'])
def mark_completed(request, task_id):
    completed = request.query_params.get('completed')
    completed_boolean = False
    #check if completed is a binary int
    if isinstance(completed, int):
        if completed >= 0 and completed <= 1:
            #set boolean value to completed_boolean
            if completed == 0:
                completed_boolean = False
            elif completed == 1:
                completed_boolean = True
            Task.objects.filter(id=task_id).update(completed=completed_boolean)
            return Response({'detail': 'Task has been marked completed.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'completed value must be either 0 or 1.'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'detail': 'completed value must be an integer.'}, status=status.HTTP_400_BAD_REQUEST)
    