from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(user= username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'credenciales incorrectos')
            return redirect('login')


    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if len(username) == 0:
            messages.info(request, 'Ingrese un nombre valido (no vacio) ')
            return redirect('register')
        elif len(email) == 0:
            messages.info(request, 'Ingrese un email valido  (no vacio) ')
            return redirect('register')  
        elif password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'usuario ya registrado')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'correo ya registrado')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name, last_name=last_name)
                user.save()
                #messages.info(request, 'usuario creado') 
        else:
            messages.info(request, 'constraseñas no coinciden ')
            return redirect('register')
        return(redirect('/'))

    
    
    else:
        return render(request, 'register.html')

        
    """
        user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name, last_name=last_name)
        user.save()
        messages.info(request, 'usuario creado')
        return(redirect('/'))
    """
