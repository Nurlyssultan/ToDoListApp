from django import forms
from django.core import validators
from ToDoApp.models import ToDoClass
class ToDoListForm(forms.ModelForm):
    class Meta():
        model = ToDoClass
        fields = '__all__'
