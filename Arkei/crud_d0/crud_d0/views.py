from django.shortcuts import render
from django.contrib.auth import authenticate, login 

'''
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'main.html', {})
        else:
            pass
        return render(request, 'outsesion/login.html', {'error': 'Invalid credentials'})

'''
def main(request):
    return render(request, 'layouts/main.html', {'titulo': 'Arkei'})

def cuenta(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'cuenta.html', {})
    return render(request, 'cuenta.html', {})

def producto(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'productos.html', {})
    return render(request, 'productos.html', {})

def registro(request):
    return render(request, 'outsesion/register.html', {})

def login(request):
    return render(request, 'outsesion/login.html', {})

def about(request):
    return render(request, 'outsesion/about.html', {})
