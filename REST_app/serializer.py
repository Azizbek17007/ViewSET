from rest_framework import serializers
from rest_framework.authtoken.admin import User

from REST_app.models import TodoItem


class TodoItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'

