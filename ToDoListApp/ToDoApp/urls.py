from django.urls import path
from ToDoApp import views

app_name = 'ToDoApp'
urlpatterns = [
    path('todo/',views.todo,name='todo'),
]
