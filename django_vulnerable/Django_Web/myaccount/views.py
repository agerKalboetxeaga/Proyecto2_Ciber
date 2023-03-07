from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from myaccount.forms import PostForm
from django.http import JsonResponse
from django.db import connection

# Create your views here.

def signup_view(request):
    error = False
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in MVC mode
            login(request, user)
            return redirect('articles:home')
        else:
            error = True
    else:
        form = UserCreationForm()
    form = UserCreationForm();
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'account/signup.html', context)




"""
def signup_view(request):
    error = False
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            if form.get_user() == None:     #Comprobar que no e
                
                username = form.data['username']    #Devuelve un objeto user
                password = form.data['password']
                with connection.cursor() as cursor:
                    sql = "INSERT INTO proyectos_usuario(username, password) VALUES(%s, %s)"    # No muy seguro 
                    cursor.execute(sql, [username, password])
                usuario= AuthenticationForm(data = request.POST).get_user()
                login(request, usuario)         #Se que no esta optimizau xd 
                return redirect('articles:home')
            else:
                error = True
        else:
            error = True
    else:
        form = UserCreationForm()
    form = UserCreationForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'account/signup.html', context)
"""
    
def login_view(request):
    error = False
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            #login the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('articles:home')
        else:
            error = True
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'account/login.html', context)

"""
def login_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            login = form.save(commit=False)
            username = login.username
            password = login.password
            print(f'username: {username} \npassword: {password}')

            with connection.cursor() as cursor:
                sql = "SELECT id, username, password FROM proyectos_usuario WHERE username = " + username + " and password= " + password # !Insecure!
                #sql = "SELECT id, username, password FROM proyectos_usuario WHERE username = %s and password = %s" No muy seguro
                #cursor.execute(sql,[username, password])
                cursor.execute(sql)
                user = cursor.fetchone()
                if user:
                    return JsonResponse({"status": "success", "user_id": user[0], "username": user[1]}, status=200)
                    #return redirect('articles:home') este el bueno; el de arriba se cambia al hacer pruebas
                else:
                     return JsonResponse({"status": "error", "message": "invalid username/password"}, status=200)

    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)
"""

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:home')