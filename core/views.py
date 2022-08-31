
from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from django.http import Http404
from django.contrib import messages
from .models import Produto, Usuario_pequi
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import EnderecoModelForm, ExtendedUserCreationForms, UserPequiForm, ProdutoModelForm, ContatoModelForm

# Create your views here.


##------> Registro e Login
def registre(request):
  if request.user.is_authenticated:
    return(redirect('/'))
  if request.method == 'POST':
    form = ExtendedUserCreationForms(request.POST)
    pequi_user_form=UserPequiForm(request.POST)

    if form.is_valid() and pequi_user_form.is_valid():
      user = form.save()

      pequi_user = pequi_user_form.save(commit=False)
      pequi_user.user = user

      pequi_user.save()

      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password = password)
      login(request, user)

      return render(request, 'index.html')

  else:
    form = ExtendedUserCreationForms()
    pequi_user_form =UserPequiForm()

  context = {'form' : form, 'pequi_user_form': pequi_user_form}
  return render(request, 'registre.html', context)
  return render(request, 'registre.html')

def create_usuario(request):
  if request.method == 'POST':
    form = ExtendedUserCreationForms(request.POST)
    pequi_user_form=UserPequiForm(request.POST)

    if form.is_valid() and pequi_user_form.is_valid():
      user = form.save()

      pequi_user = pequi_user_form.save(commit=False)
      pequi_user.user = user

      pequi_user.save()

      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password = password)
      login(request, user)

      return render(request, 'index.html')

  else:
    form = ExtendedUserCreationForms()
    pequi_user_form =UserPequiForm()

  context = {'form' : form, 'pequi_user_form': pequi_user_form}
  return render(request, 'registre.html', context)

@login_required(login_url='/login')
def logout_user(request):
  logout(request)
  return redirect('/')

def login_user(request):
  if request.user.is_authenticated:
    return redirect('/')
  return render(request, 'login.html')

def login_submit(request):
  if request.method == 'POST':
    if request.POST:
      usuario = request.POST.get('usuario')
      senha = request.POST.get('senha')
      user = authenticate(username=usuario, password=senha)
      if user:
        messages.success(request, 'Login com sucesso')
        login(request,user)
        return redirect('/')
      else:
        messages.error(request,'Error')
        return render(request, 'login.html')
  messages.error(request, 'erro ao logar')
  return render(request, 'login.html')


##-----> Registro de produtos
#implementar a quebra para não usuários
def produto(request):
  if not request.user.is_authenticated:
    raise Http404
  if request.method == 'POST':
    form = ProdutoModelForm(request.POST, request.FILES)
    if form.is_valid():
      instance = form.save(commit=False)

      instance.user_produtor = request.user

      instance.save()

      messages.success(request, 'Produto cadastrado com sucesso')
      form = ProdutoModelForm()
    else:
      messages.error(request, 'Erro ao salvar produto')
  else:
    form = ProdutoModelForm()
  context = {'form':form }
  return render(request, 'produto.html', context)

def produto_submit(request):
  if not request.user.is_authenticated:
    raise Http404

  if request.method == 'POST':
    form = ProdutoModelForm(request.POST, request.FILES)
    if form.is_valid():
      instance = form.save(commit=False)

      instance.user_produtor = request.user

      instance.save()
      messages.success(request, 'Deu certo cadastrar')
      return redirect('/')
    else:
      messages.error(request, 'Erro ao salvar produto')
      return redirect(request, 'produto.html')
  else:
    return redirect('index')

##------> Registro de endereços

def cadastro_endereco(request):
  if not request.user.is_authenticated:
    raise Http404
  if request.method == 'POST':
    form = EnderecoModelForm(request.POST, request.FILES)
    if form.is_valid():
      instance = form.save(commit=False)

      instance.user_endereco = request.user

      instance.save()

      messages.success(request, 'Endereco cadastrado com sucesso')
      form = EnderecoModelForm()
    else:
      messages.error(request, 'Erro ao salvar endereco')
  else:
    form = EnderecoModelForm()
  context = {'form':form }
  return render(request, 'produto.html', context)

def endereco_submit(request):
  if not request.user.is_authenticated:
    raise Http404

  if request.method == 'POST':
    form = EnderecoModelForm(request.POST, request.FILES)
    if form.is_valid():
      instance = form.save(commit=False)

      instance.user_endereco = request.user

      instance.save()
      messages.success(request, 'Deu certo cadastrar')
      return redirect('/')
    else:
      messages.error(request, 'Erro ao salvar produto')
      return redirect(request, 'produto.html')
  else:
    return redirect('index')

##-------> Registro de contatos
def cadastro_contato(request):
  if not request.user.is_authenticated:
    raise Http404
  if request.method == 'POST':
    form = ContatoModelForm(request.POST, request.FILES)
    if form.is_valid():
      instance = form.save(commit=False)

      instance.user_contato = request.user

      instance.save()

      messages.success(request, 'Contato cadastrado com sucesso')
      form = ContatoModelForm()
    else:
      messages.error(request, 'Erro ao salvar Contato')
  else:
    form = ContatoModelForm()
  context = {'form':form }
  return render(request, 'contato.html', context)

def contato_submit(request):
  if not request.user.is_authenticated:
    raise Http404

  if request.method == 'POST':
    form = ContatoModelForm(request.POST, request.FILES)
    if form.is_valid():
      instance = form.save(commit=False)

      instance.user_contato = request.user

      instance.save()
      messages.success(request, 'Deu certo cadastrar')
      return redirect('/')
    else:
      messages.error(request, 'Erro ao salvar contato')
      return redirect(request, 'contato.html')
  else:
    return redirect('index')

##------> Home Page e debugger
def index(request):
  produtos = Produto.objects.all()
  context = {
    "Produtos" : produtos
  }
  return render(request, 'index.html', context)
