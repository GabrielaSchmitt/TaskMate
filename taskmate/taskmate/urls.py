# taskmate/urls.py
from django.contrib import admin
from django.urls import path, include
from tasks import views  # Importando as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),  # Definindo o dashboard como a página inicial
    path('tasks/', include('tasks.urls')),  # Incluindo URLs da aplicação tasks
    path('me/', views.me, name='me'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
