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


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
