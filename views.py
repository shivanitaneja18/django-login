# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views import generic
from django.views.generic import views
from .forms import UserForm



# Create your views here.
class UserFromView(View):
    form_class=UserForm
    template_name='music/registration_form.html'
    
    #display a blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})
        
    #process form data

    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            
    #cleaned (normalised) data
    username= form.cleaned_data['username']
    password= form.cleaned_data['password']
    user.set_password(password)
    user.save()


    #returns User objects if credentials are correct

    user=authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return redirect('music:Index')

            return render(request,self.template_name,{'form':form
            })


    


