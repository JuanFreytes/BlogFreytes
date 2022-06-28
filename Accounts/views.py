from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import BlogUserForm, EditFullUser
from django.contrib.auth.decorators import login_required
from .models import UserExtension

def my_login(request):
    msj = ''
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                msj = 'El usuario no se pudo autenticar.'
        else:
            msj = 'El formulario no es valido.'
    
    
    login_form = AuthenticationForm()
    return render(request, 'Accounts/login.html', {'login_form': login_form, 'msj': msj}) #chequear!

def register(request):
    
    if request.method == 'POST':
        form = BlogUserForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return redirect('login')
        else:
            return render(request, 'Accounts/register.html', {'form': form, 'msj': 'El formulario no es valido.'})
            
    
    form = BlogUserForm()
    return render(request, 'Accounts/register.html', {'form': form})

@login_required
def edit_user(request):
    
    user_extension_logued, _ = UserExtension.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = EditFullUser(request.POST, request.FILES)
        
        if form.is_valid():
            
            request.user.email = form.cleaned_data['email']
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']
            if form.cleaned_data['avatar'] is not None:
                user_extension_logued.avatar = form.cleaned_data['avatar']
            user_extension_logued.link = form.cleaned_data['link']
            
            if form.cleaned_data['password1'] != '' and form.cleaned_data['password1'] == form.cleaned_data['password2']:
                request.user.set_password(form.cleaned_data['password1'])
            
            request.user.save()
            user_extension_logued.save()
            
            return redirect('index')
        else:
            return render(request, 'Accounts/edit.html', {'form': form, 'msj': 'El formulario no es valido.'})
            
    
    form = EditFullUser(
        initial={
            'email': request.user.email,
            'password1': '',
            'password2': '',
            'first_name': request.user.first_name,
            'last_name': request.user.last_name, 
            'avatar': user_extension_logued.avatar,
            'link': user_extension_logued.link,
        }
    )
    return render(request, 'Accounts/edit.html', {'form': form})

@login_required
def user_data(request):
    #usuario = UserExtension.objects.get(id=pk)
    user_extension_logued, _ = UserExtension.objects.get_or_create(user=request.user)
    form = {
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name, 
            'avatar': user_extension_logued.avatar,
            'link': user_extension_logued.link,
        }
    return render(request, 'Accounts/user_data.html', {'usuario':form})
