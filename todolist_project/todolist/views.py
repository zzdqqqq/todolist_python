from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    '''
    test
    '''
    return HttpResponse('welcome to to-do list')
