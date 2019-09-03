'''
    set a serializer to communicate with frontend by http and json
'''

from rest_framework import serializers
from .models import TodoModel

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = '__all__'
        