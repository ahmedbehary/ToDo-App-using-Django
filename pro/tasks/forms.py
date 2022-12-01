from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Add new item..' , 'class':'form-control' }))
    # complete = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    class Meta:
        model = Task 
        fields = '__all__'
        
