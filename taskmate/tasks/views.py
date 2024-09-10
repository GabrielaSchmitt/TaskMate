from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm, TaskForm
from .models import Task

# Home page
def index(request):
    return render(request, 'index.html')

# Signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a página de login após o cadastro
        else:
            # Adiciona erros ao formulário, se houver
            print(form.errors)  # Adicione isso para depurar
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


# Login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Logout page
def user_logout(request):
    logout(request)
    return redirect('login')

# Task list page
# tasks/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task


def task_list(request):
    user = request.user

    # Obtendo todas as tarefas atribuídas ao usuário e tarefas públicas
    user_tasks = Task.objects.filter(assigned_to=user)
    public_tasks = Task.objects.filter(is_public=True).exclude(assigned_to=user)

    # Combine as tarefas do usuário e as públicas
    tasks = user_tasks | public_tasks

    # Verifique o que está sendo passado para o template
    print(tasks)

    return render(request, 'task_list.html', {'tasks': tasks, 'user': user})


@login_required
def public_tasks(request):
    status_filter = request.GET.get('status')
    tasks = Task.objects.filter(is_public=True)  # Apenas tarefas públicas

    if status_filter:
        tasks = tasks.filter(status=status_filter)

    return render(request, 'public_task_list.html', {'tasks': tasks})


# Create task page
from django.shortcuts import render, redirect
from .forms import TaskForm

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user  # Define o usuário logado como criador
            task.save()  # Salva a tarefa
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})


# Edit task page
@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form, 'task': task})


# Delete task page
@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, assigned_to=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})

@login_required
def dashboard(request):
    status_filter = request.GET.get('status')
    tasks = Task.objects.filter(is_public=True)

    if status_filter:
        tasks = tasks.filter(status=status_filter)

    return render(request, 'dashboard.html', {'tasks': tasks})


