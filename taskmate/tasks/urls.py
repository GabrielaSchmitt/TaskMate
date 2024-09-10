from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='home'),  # Lista de tarefas do usuário e públicas
    path('public/', views.public_tasks, name='public_tasks'),  # Lista de tarefas públicas
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
]

