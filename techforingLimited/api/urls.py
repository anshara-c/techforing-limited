from django.urls import path 
from .views import user_detail,register_user, get_users,projects, project_detail, tasks, task_detail, comments, comment_detail
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('users/<int:id>', user_detail, name='user_detail'),
    path('users/all/', get_users, name='get_users'),
    path('users/register/', register_user, name='register_user'),
    path('projects/', projects, name='projects'),
    path('projects/<int:id>/', project_detail, name='project_detail'),
    path('projects/<int:id>/tasks/', tasks, name='tasks'),
    path('tasks/<int:id>/', task_detail, name='task_detail'),
    path('tasks/<int:id>/comments/', comments, name="comments"),
    path('comments/<int:id>/', comment_detail, name="comment_detail"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]