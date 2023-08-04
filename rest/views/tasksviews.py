from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from rest.permissions import IsOwner
from rest.serializers.taskserializers import TaskSerializer, TaskCreateSerializer, TaskDetailSerializer
from tasks.models import Task


class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwner, IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TaskCreateSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskSingle(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    permission_classes = [IsOwner, IsAuthenticated]

class TaskDelete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    permission_classes = [IsOwner, IsAuthenticated]
    
class ExecuteTask(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwner, IsAuthenticated]
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.complete = True
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
class TaskUpdate(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    permission_classes = [IsOwner, IsAuthenticated]
