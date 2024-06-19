from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoItemModelViewSet

router = DefaultRouter()
router.register('todoitem', TodoItemModelViewSet, basename='todoitem')
