from django import forms
from django.forms import fields
from .models import Student
from blog import models


class StudentRegisterForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter Name", 'class': "form-input"}))
    stage = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter Stage", 'class': "form-input"}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': "Enter Age", 'class': "form-input"}))


    class Meta:
        model = Student
        fields = ['name', 'stage', 'age', 'image']

class SearchForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': "Search by id", 'class': "searchFormInput"}))
    
    class Meta:
        model = Student
        fields = ['id']

class EditForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-input"}))
    stage = forms.CharField(widget=forms.TextInput(attrs={'class': "form-input"}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-input"}))

    class Meta:
        model = Student
        fields = ['name', 'stage', 'age', 'image']