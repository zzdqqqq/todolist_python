'''
    register title, description, checkbox and createdDate to django admin
'''

from django.contrib import admin
from .models import TodoModel

class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'completed', 'createdDate']

admin.site.register(TodoModel, admin_class=TodoAdmin)
