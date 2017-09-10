from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from models import Task
from rest_framework.renderers import JSONRenderer
from serializers import TaskSerializer


class TaskCreateAPIView(APIView):
    def post(self, request):
        task_name = request.data['name']
        if task_name:
            task = Task.objects.create(name=task_name)
            task.save()
            return Response({'data': 'Task created'}, status=status.HTTP_200_OK)
        else:
            return Response({'data': 'task_name required'}, status=status.HTTP_400_BAD_REQUEST)


class TaskDeleteAPIView(APIView):
    def post(self, request):
        id = request.data['task']
        if id:
            task = Task.objects.get(id=id)
            task.delete()
            return Response({'data': 'Successfully deleted task'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Please add id to request'}, status=status.HTTP_400_BAD_REQUEST)


class TaskAllAPIView(APIView):
    def post(self, request):
        print request.data

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        print serializer.data
        task_data = JSONRenderer().render(serializer.data)
        print task_data
        return Response(task_data)


class TaskCompletedAPIView(APIView):
    def get(self, request):
        tasks = Task.objects.filter(is_completed=False)
        serializer = TaskSerializer(tasks, many=True)
        task_data = JSONRenderer().render(serializer.data)
        return Response(task_data)

    def post(self, request):
        task = request.data['task']
        if task:
            Task.objects.filter(id=task).update(is_completed=True)
            return Response({'data': 'Task marked as completed.'}, status=status.HTTP_200_OK)
        else:
            return Response({'data': 'Task id required'}, status=status.HTTP_400_BAD_REQUEST)