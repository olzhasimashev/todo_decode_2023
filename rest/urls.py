from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest.views.tasksviews import TaskListCreate, TaskSingle, TaskDelete, ExecuteTask, TaskUpdate

urlpatterns = [
    path('todo/', TaskListCreate.as_view()),
    path('todo/<pk>/', TaskSingle.as_view()),
    path('todo/<pk>/', TaskDelete.as_view()),
    path('todo/<pk>/execute/', ExecuteTask.as_view()),
    path('todo/update/<pk>/', TaskUpdate.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
