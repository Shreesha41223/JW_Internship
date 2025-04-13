from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    tasks = Todo.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        completed = request.POST.get('completed', False)
        todo = Todo(title=title, completed=completed)
        todo.save()
        return redirect('index')
    return redirect('index')

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')

def complete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('index')