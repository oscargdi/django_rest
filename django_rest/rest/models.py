from datetime import datetime

from django.db import models

# Create your models here.


class Project(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    due_date = models.DateTimeField(default=datetime.now)
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
