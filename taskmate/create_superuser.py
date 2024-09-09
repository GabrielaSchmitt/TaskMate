import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskmate.settings')
django.setup()

from django.contrib.auth.models import User

# Defina as informações do superusuário
username = 'admin'
email = 'admin@example.com'
password = '123'

# Crie o superusuário se ele não existir
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'Superuser {username} criado com sucesso!')
else:
    print(f'Superuser {username} já existe.')
