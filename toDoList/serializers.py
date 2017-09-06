from rest_framework import serializers
from models import Task


class TaskSerializer(serializers.Serializer):
    begin = serializers.DateTimeField()
    end = serializers.DateTimeField()
    name = serializers.CharField()
    is_completed = serializers.BooleanField()

    class Meta:
        model = Task
        fields = ('begin', 'end', 'name', 'is_completed')