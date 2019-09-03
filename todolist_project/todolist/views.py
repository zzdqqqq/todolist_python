# from django.shortcuts import render

# # Create your views here.
# def index(request):
#     '''
#     test
#     '''
#     return render(request, 'todolist/index.html')

from rest_framework import generics, viewsets
from todolist.models import TodoModel
from todolist.serializers import TodoSerializer

# app_name = 'todolist'
class TodoViewSet(viewsets.ModelViewSet):
    """
        @param: queryset: Get all objects from TodoModel
        @param: serializer_class: (from todolist.serializers)
    """
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer

class TestViewSet(viewsets.ModelViewSet):
    """
        test
    """
    pass