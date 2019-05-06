from django.shortcuts import render
from ToDoApp.models import ToDoClass
# Create your views here.
def index(request):
    return render(request,'ToDoApp/index.html')
def todo(request):
    toDoList = ToDoClass.objects.all()
    toDo_dict = {'contents':toDoList}
    return render(request,'ToDoApp/todolist.html', context = toDo_dict)
