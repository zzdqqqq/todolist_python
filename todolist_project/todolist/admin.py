'''
    register title, description and checkbox to django admin
'''

from django.contrib import admin
from .models import TodoModel

class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'completed']
    # list_display = ['title', 'description', 'created_time', 'check_box']

admin.site.register(TodoModel, admin_class=TodoAdmin)
