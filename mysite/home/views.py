from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User

from home.models import UserProfile
from home.forms import SignUpForm

def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            return redirect ('login')
        else:
            form = AuthenticationForm()
        return render(request, 'polls/home.html', {'form': form})
    else:
        return redirect('home')

def home(request):
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(
            user_id=request.user.pk
        )
        request.session['saldo'] = user_profile.valor_market_balance
        
        return render(request, 'polls/Dev-uy.html')
    else:
        return redirect('login')
    

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                auth_login(request, user)
                return redirect('home')
        else:
            form = SignUpForm()
        return render(request, 'home/signup.html', {'form': form})
    else:
        return redirect('home')

def logout(request):
    auth_logout(request)
    return redirect('login')

def tienda(request):
    userProf, created = UserProfile.objects.get_or_create(user_id=request.user.id)
    saldo = userProf.valor_market_balance
    saldo_str = str(saldo)
    user_id = request.user.id
    id_str = str(user_id)
    new_port='8080'
    hostname = request.get_host().split(':')[0]
    url = 'http://' + hostname + ':' + new_port + '/guardar/' + id_str + '/' + saldo_str + '/'
    return redirect(url)

def saldo(request, id_user, saldo):
    user = get_object_or_404(User, id=id_user)
    auth_login(request, user)
    
    userProf, created = UserProfile.objects.get_or_create(user_id=id_user)
    userProf.valor_market_balance = saldo

    return redirect('home')
