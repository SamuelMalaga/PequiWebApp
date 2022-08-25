from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Usuario_pequi
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ExtendedUserCreationForms, UserPequiForm

# Create your views here.

def registre(request):
  if request.user.is_authenticated:
    return(redirect('/'))
  return render(request, 'registre.html')

def create_usuario(request):
  if request.method == 'POST':
    form = ExtendedUserCreationForms(request.POST)
    pequi_user_form =UserPequiForm(request.POST)

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


  # if request.POST:
  #   if not request.POST.get('password1'):
  #     return render(request, 'registre.html')
  #   if not request.POST.get('password2'):
  #     return render(request, 'registre.html')
  #   if request.POST.get('password1') == request.POST.get('password2'):
  #       user = User.objects.create(
  #         username = request.POST.get('username'),
  #         email = request.POST.get('email'),
  #         first_name = request.POST.get('first_name')
  #         )
  #       user.set_password(request.POST.get('password1'))
  #       user.save()
  #       login(request, user)
  #       return redirect('/')
  #   else:
  #     return render(request, 'registre.html')

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


def index(request):
  # print('VEIO DO USER',dir(request.user))
  # print('VEIO DO USER PEQUI',dir(request.user.usuario_pequi))
  # print('Teste __str__',request.user.usuario_pequi.__str__ )
  return render(request, 'index.html')

# def produto_submit(request):
#   if request.method == 'POST':
#     form = ProdutoModelForms(request.POST, request.FILES)
#     if form.is_valid():
#         form.save()
#         return redirect('index')
#     else:
#       messages.error(request, 'Erro ao salvar produto')
#       return render(request, 'index.html')
#   else:
#     return redirect('index')

# def usuario_submit(request):
#   if request.method == 'POST':
#     form = UsuarioModelForms(request.POST, request.FILES)
#     if form.is_valid():
#         pass
#   else:
#     return redirect('index')
