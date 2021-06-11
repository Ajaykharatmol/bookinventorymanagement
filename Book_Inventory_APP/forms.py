from django.forms import ModelForm
from django import forms
from .models import Books

class BooksForm(forms.ModelForm):
	class Meta:
		model = Books
		fields = ['book_name', 'description',]

		widgets = {
            'book_name' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.TextInput(attrs={'class':'form-control'}),
             }  