'''
    set up models
'''
from django.db import models

class TodoModel(models.Model):
    title = models.TextField()
    description = models.TextField()
    completed = models.BooleanField(default=False)
    # created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
