from .models import *

from django.shortcuts import render,redirect,get_object_or_404

def addpage(request):
  if request.method == "POST":
      name = request.POST.get('name')
      description = request.POST.get('description')
      date_limit = request.POST.get('date_limit')
      confirm = request.POST.get('confirm') == 'on'
      todo = Todo(nome=name, descricao=description, data_limite=date_limit, status=confirm)
      todo.save()
      return redirect('list')
  else:
    return render(request, 'add.html')
def listpage(request):
  tasks = Todo.objects.all()
  return render(request, 'list.html',{'tasks':tasks})

def delete_task(request,task_id):
   if request.method == "POST":
      task = get_object_or_404(Todo, id=task_id)
      task.delete()
      return redirect('list')

def edit_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id)
    if request.method == "POST":
        task.nome = request.POST.get('name')
        task.descricao = request.POST.get('description')
        task.data_limite = request.POST.get('date_limit')
        task.status = request.POST.get('confirm') == 'on'
        task.save()
        return redirect('list')
    else:
        return render(request, 'edit.html', {'task': task})