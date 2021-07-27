from django.shortcuts import render
from .models import ToDoListItems
from django.http import HttpResponseRedirect 
# Create your views here.

def appview(request):
    all_todo_items = ToDoListItems.objects.all()
    return render(request,'todo_list.html',{'all_items' : all_todo_items })

def addTodoView(request):
    x = request.POST['content']
    new_item = ToDoListItems(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/') 

def deleteTodoView(request, i):
    y = ToDoListItems.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todoapp/') 