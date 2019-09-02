'''
    app's urls.py
'''

from django.conf.urls import url
from . import views

app_name = 'todolist'
urlpatterns = [
    url(r'^$', views.index, name='index')
]
