from django.shortcuts import render
from ToDoApp.models import ToDoClass
# Create your views here.
def index(request):
    return render(request,'ToDoApp/index.html')
def todo(request):
    toDoList = ToDoClass.objects.all()
    toDo_dict = {'contents':toDoList}
    return render(request,'ToDoApp/todolist.html', context = toDo_dict)
def toDoListView(request):
    if request.method == 'POST':
        c = request.POST['content']
        print(c)
        print(ToDoClass.objects.all())
        print(ToDoClass.objects.all().filter(content = c).exists())
        if ToDoClass.objects.all().filter(content = c).exists() != True:
            toDoTask = ToDoClass(content = c)
            toDoTask.save()
        return todo(request)
    else:
        print('Error:NOT POST')
def DeleteATaskView(request):
        if request.method == 'POST':
            deleteTaskId = request.POST['num']
            deleteTask = ToDoClass.objects.get(id = deleteTaskId)
            deleteTask.delete()
            return todo(request)
        else:
            print('Error:NOT POST')
