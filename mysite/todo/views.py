from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from todo.models import Todo
from todo.serializer import TodoSerializer


@api_view(['GET'])
def test(request):
    return Response({'test': 'success'})


class TodoListViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
