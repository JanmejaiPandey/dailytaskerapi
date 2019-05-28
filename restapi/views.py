from django.shortcuts import render
from rest_framework import viewsets
from django.http import request
from .models import Tasks
from .serializers import TaskSerializer

class TaskView(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
