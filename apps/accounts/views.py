from django.contrib.auth import login, authenticate, forms, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.db import models

class Login(View):
    form = forms.AuthenticationForm
    def get(self, request):
        form = self.form(None, request.POST)
        context = {'form' : form}
        return render(request, 'accounts/login.html', context)
    def post(self, request):
        form = self.form(None, request.POST)
        context ={'form': form}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/travels')
            else:
                return render(request, 'accounts/login.html', context)
        else:
            return render(request, 'accounts/login.html', context)

class Register(View):
    form = forms.UserCreationForm
    def get(self, request):
        context = {'form' : self.form()}
        print context
        return render(request, 'accounts/register.html', context)
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            print "save new user"
            form.save()
            return redirect('/login')
        else:
            context = {'form' : form}
            return render(request,'accounts/register.html', context)

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/login')

class Success(View):   
    template = 'accounts/success.html'
    user = ''
    context = {'templateData' : user}
    def get(self, request):
        return render(request, self.template, self.context)
