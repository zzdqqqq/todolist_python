from rest_framework import generics, viewsets
from todolist.models import TodoModel
from todolist.serializers import TodoSerializer

# app_name = 'todolist'
class TodoViewSet(viewsets.ModelViewSet):
    """
        @param: queryset: Get all objects from TodoModel
        @param: serializer_class: (from todolist.serializers)
    """
    queryset = TodoModel.objects.order_by("-createdDate", "title")
    serializer_class = TodoSerializer