from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages, auth
import re
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if len(senha) < 8:
            messages.add_message(request, constants.ERROR, 'Sua senha deve conter 8 ou mais caractertes')
            return redirect('/cadastro')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/cadastro')

        if not re.search('[A-Z]',senha):
            messages.add_message(request, constants.ERROR, 'Sua senha não contem letras maiúsculas')
            return redirect('/cadastro')

        if not re.search('[a-z]', senha):
            messages.add_message(request, constants.ERROR, 'Sua senha não contem letras minúsculas')
            return redirect('/cadastro')

        if not re.search('[1-9]', senha):
            messages.add_message(request, constants.ERROR, 'Sua senha não contém números')
            return redirect('/cadastro')


        if usuario or email:
            if usuario:
                messages.add_message(request, constants.ERROR, 'Esse usuário já existe')
            if email:
                messages.add_message(request, constants.ERROR, 'Esse e-mail já está cadastrado')
            return redirect('/cadastro')

        try:
            usuario = User.objects.create_user(username=usuario,
                                            email=email,
                                            password=senha)
            usuario.save()
            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso !!!')
            return redirect('/cadastro')
        except:
            messages.add_message(request, constants.WARNING, 'Erro interno do sistema')
            return redirect('/cadastro')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        usuario = auth.authenticate(request, username=usuario, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Usuário inválido')
            return redirect('/login')
        else:
            # se o usuário existe no banco de dados, é feita a autenticação
            auth.login(request, usuario)
            return redirect('/home')

