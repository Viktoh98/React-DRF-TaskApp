from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Task
from . api.serializers import TaskSerializer, TaskListSerializer
from . utils import CustomAuthPermissionsMixin


class TaskListCreateView(APIView, CustomAuthPermissionsMixin):
    serializer_class = TaskListSerializer

    def get(self, request):
        user = request.user
        tasks = Task.objects.all(updated_by=user)
        serializer = self.serializer_class(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            cleaned_data = serializer.validated_data
            slug = cleaned_data['name']
            serializer.save(slug=slug)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class TaskDetailUpdateView(APIView, CustomAuthPermissionsMixin):
    serializer_class = TaskSerializer

    def get_object(self, request, slug):
        try:
            return Task.objects.get(slug=slug, updated_by=request.user)
        except:
            raise Http404

    def get(self, request, slug):
        task = self.get_object(request, slug)
        serializer = self.serializer_class(task)
        return Response(serializer.data)

    def put(self, request, slug):
        task = self.get_object(request, slug)
        serializer = self.serializer_class(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, slug):
        task = self.get_object(request, slug)
        task.delete()
        return Response([{'message': 'successful'}], status=200)
