from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer

# Create your views here.


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer = TaskSerializer
