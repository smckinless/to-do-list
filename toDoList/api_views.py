from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from models import Task
from rest_framework.renderers import JSONRenderer
from serializers import TaskSerializer


class TaskCreateAPIView(APIView):
    def post(self, request):
        task_name = request.data['name']



class TaskDeleteAPIView(APIView):
    def post(self, request):
        print request.data


class TaskAPIView(APIView):
    def post(self, request):
        print request.data

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        print serializer.data
        task_data = JSONRenderer().render(serializer.data)
        print task_data
        return Response(task_data)
