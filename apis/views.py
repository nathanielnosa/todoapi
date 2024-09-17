from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response

from .serializers import *

from . models import Todo

# Create your views here.
class TodoView(APIView):
    def post(self, request):
        try:
            serializer = TodoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            todos = Todo.objects.all()
            serializer = TodoSerializer(todos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

        
# Create your views here.
class TodoDetail(APIView):
    def get(self,request,*args, **kwargs):
        todo_id = kwargs.get('id')
        try:
            todo = Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return Response({"res":"Object with the id does not exist"},status=status.HTTP_400_BAD_REQUEST)
        serializer = TodoSerializer(todo)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,*args,**kwargs):
        todo_id = kwargs.get('id')
        try:
            todo = Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return Response({"res":"Object with the id does not exist"},status=status.HTTP_400_BAD_REQUEST)
        
        serializer = TodoSerializer(instance=todo,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,*args,**kwargs):
        todo_id = kwargs.get('id')
        try:
            todo = Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return Response({"res":"Object with the id does not exist"},status=status.HTTP_400_BAD_REQUEST)
        
        todo.delete()
        return Response({"res":"Object with the id delete"},status=status.HTTP_200_OK)
