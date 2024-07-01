from django import forms 
from task.models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title" , "description","complete"]
