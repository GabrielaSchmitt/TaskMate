from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm, TaskForm
from .models import Task

@login_required
def dashboard(request):
    user = request.user
    status_filter = request.GET.get('status')
    tasks = Task.objects.filter(created_by=user)
    userIsAdmin = user.is_superuser
    users = []
    
    if userIsAdmin:
        users = User.objects.all()
    
    if status_filter:
        tasks = tasks.filter(status=status_filter)

    return render(request, 'index.html', {
        'tasks': tasks,
        'status_filter': status_filter,
        'status_choices': Task.STATUS_CHOICES, 
        'user': user,
        'userIsAdmin': userIsAdmin,
        'users': users
    })

@login_required
def user_tasks(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    tasks = Task.objects.filter(created_by=user)
    status_filter = request.GET.get('status')
    request_user_is_admin = request.user.is_superuser
    
    if(not request_user_is_admin):
        return redirect('home')

    if status_filter:
        tasks = tasks.filter(status=status_filter)

    return render(request, 'user_tasks.html', {
        'tasks': tasks,
        'status_filter': status_filter,
        'status_choices': Task.STATUS_CHOICES,
        'user': user,
    })

@login_required
def me(request):
    user = request.user
    return render(request, 'me.html', {'user': user})

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

def task_list(request):
    user = request.user
    status_filter = request.GET.get('status')
    from django.db.models import Q
    user_tasks = Task.objects.filter(Q(is_public=True) | Q(created_by=request.user))
    
    if status_filter:
        user_tasks = user_tasks.filter(status=status_filter)

    return render(request, 'task_list.html', {
        'tasks': user_tasks, 
        'status_filter': status_filter, 
        'status_choices': Task.STATUS_CHOICES, 
        'user': user
    })

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