from django.contrib.auth.models import User
from django import forms



class UserForm(forms.ModelForm):
	password=forms.Charfield(widget=forms.PasswordInput)

	class Meta:
	model=User
	fields= ['username','email','password']
	
