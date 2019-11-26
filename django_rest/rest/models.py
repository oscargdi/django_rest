from django.db import models

# Create your models here.


class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    due_date = models.DateTimeField(null=True)
