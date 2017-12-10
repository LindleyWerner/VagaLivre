from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
import requests
import json
from .forms import *

from django.views.decorators.csrf import csrf_exempt


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return index(request)
    return render(request, 'login.html')


def logout_user(request):
        logout(request)
        return index(request)


def index(request):
    if request.user.is_authenticated():
        context = {'is_auth': True}
    else:
        context = {'is_auth': False}
    MY_URL = 'https://vaga-livre.herokuapp.com/vagas2/30130183'
    r = requests.get(MY_URL)
    face = r.json()
    posicoes = face["result"]
    context['vagas'] = posicoes[:7]
    context['vagas1'] = posicoes[7:30]
    context['vagas2'] = posicoes[30:]
    return render(request, 'index.html', context)



@csrf_exempt
def search(request):
    MY_URL = 'https://vaga-livre.herokuapp.com/vagas2/30130183'
    r = requests.get(MY_URL)
    face = r.json()
    posicoes = face["result"]
    return render(request, 'index.html', {'vagas': posicoes})


def cadastrar_usuario(request):
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'cadastrarusuario.html', context)



