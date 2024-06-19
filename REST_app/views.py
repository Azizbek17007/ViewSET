from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from REST_app.models import TodoItem
from REST_app.serializer import TodoItemModelSerializer


# Create your views here.



class TodoItemModelViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TodoItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

