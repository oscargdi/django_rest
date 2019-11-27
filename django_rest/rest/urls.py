from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('tasks', views.TaskView)
router.register('tags', views.TagView)
router.register('projects', views.ProjectView)

urlpatterns = [
    path('', include(router.urls))
]
