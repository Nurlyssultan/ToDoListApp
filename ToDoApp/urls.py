from django.urls import path
from ToDoApp import views

app_name = 'ToDoApp'
urlpatterns = [
    path('toDoList/',views.toDoListView),
    path('DeleteATask/',views.DeleteATaskView),
    path('todo/',views.todo,name='todo'),
]
