from rest_framework import serializers
from models import Task


class TaskSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    begin = serializers.DateTimeField()
    end = serializers.DateTimeField()
    name = serializers.CharField()
    is_completed = serializers.BooleanField()

    class Meta:
        model = Task
        fields = ('id', 'begin', 'end', 'name', 'is_completed')