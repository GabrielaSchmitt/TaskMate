from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('public/', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('user/<int:user_id>/', views.user_tasks, name='user_tasks'),  # Nova rota
]
