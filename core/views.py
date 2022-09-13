
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, HttpResponseRedirect
from django.http import Http404
from django.contrib import messages
from django.urls import reverse

from .filters import ProdutoFilter
from .models import Contato, Produto, Usuario_pequi,ProdutoReview, Cart
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import AtualizacaoCadastroForm, EnderecoModelForm, ExtendedUserCreationForms, ReviewForms, UserPequiForm, ProdutoModelForm, ContatoModelForm, AtualizacaoUserPequi, ProdutoAddCarrinhoForm
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_POST
from .cart import Carrinho

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

##------>Visualização de detalhes do produto e envio de review
def produto_detalhe(request, id):
  produto= Produto.objects.get(id = id)
  produto_carrinho_form = ProdutoAddCarrinhoForm()
  context = {
    'produto': produto,
    'form':produto_carrinho_form

  }
  return render(request,'detalhe_produto.html', context)

def submit_review(request, id):
  url = request.META.get('HTTP_REFERER')
  form = ReviewForms(request.POST)
  if form.is_valid():
    data = form.save(commit=False)
    data.produto_rating = Produto.objects.get(id=id)
    data.usuario_rating = request.user
    data.texto_avaliacao = form.cleaned_data['texto_avaliacao']
    data.nota_avaliacao = form.cleaned_data['nota_avaliacao']
    data.save()
    messages.success(request, 'Review feita!')
    return redirect(url)

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
  return render(request, 'cadastro_endereco.html', context)

def remover_endereco(request, endereco_id):
  pass

def endereco_submit(request):
  print('endereco submit')
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
      return redirect(request, 'cadastro_endereco.html')
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

def remover_contato(request, contato_id):
  pass

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
##------>Página de ajuda
def ajuda(request):
  return render(request, 'ajuda.html')
##------>Sobre Nós
def sobre(request):
  return render(request, 'sobre.html')
##------>Minha conta
def minha_conta(request, id):
  if not request.user.is_authenticated:
    raise Http404
  else:
    usuario = User.objects.get(id=id)
    meus_produtos = Produto.objects.filter(user_produtor__exact = usuario.id)
    meus_contatos = Contato.objects.filter(user_contato__exact = usuario.id)
    context = {
      'usuario': usuario,
      'produtos_usuario': meus_produtos,
      'meus_contatos' : meus_contatos
    }
  return render(request, 'minha_conta.html',context)

def alterar_dados_conta(request):
  user_ref = request.user
  form_user = AtualizacaoCadastroForm(instance=request.user)
  form_user_pequi = UserPequiForm(instance=request.user.usuario_pequi)
  if request.method == 'POST':
    form_user = AtualizacaoCadastroForm(request.POST,instance=request.user)
    form_user_pequi = UserPequiForm(request.POST,instance=request.user.usuario_pequi)

    if form_user.is_valid() and form_user_pequi.is_valid():
      form_user.save()
      form_user_pequi.save()
  context = {'form': form_user, 'form_user_pequi': form_user_pequi, 'user_ref': user_ref }
  return render(request, 'editar_cadastro.html', context)

def alterar_dados_produto(request, produto_id):
  user_ref=request.user
  produto= Produto.objects.get(id = produto_id)
  form_produto = ProdutoModelForm(instance=produto)
  if request.method =='POST':
    form_produto = ProdutoModelForm(request.POST, instance=produto)
    if form_produto.is_valid():
      form_produto.save()
  context = {
    'form_produto' : form_produto,
    'produto': produto,
    'user_ref': user_ref
  }
  return render(request, 'editar_produto.html', context)

def remover_produto(request, produto_id):
  id = request.user.id
  produto = Produto.objects.get(pk=produto_id)
  produto.delete()
  return redirect('minha_conta', id = id)

def pagina_produtos(request):
  produtos_list = Produto.objects.all().order_by('id')
  produtos_filtro = ProdutoFilter(request.GET, queryset=produtos_list)

  paginator = Paginator(produtos_filtro.qs, 10)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  try:
        produtos = paginator.page(page_number)
  except PageNotAnInteger:
        produtos = paginator.page(1)
  except EmptyPage:
        produtos = paginator.page(paginator.num_pages)
  context = {
    "Produtos" : produtos,
    "Page": page_obj,
    "meuFiltro" : produtos_filtro
  }
  return render(request, 'pagina_produtos.html', context)


##------>Profile View (parte do carrinho)
def cart_home(request):
  carrinho = Carrinho(request)
  context = {
    'carrinho': carrinho
  }
  for item in carrinho:
    print(item)

  return render(request,'carrinho.html', context)

# def cart_update(request):
#     product_id = 18
#     # Pega o produto com id 5
#     product_obj = Produto.objects.get(id=product_id)
#     # Cria ou pega a instância já existente do carrinho
#     cart_obj, new_obj = Cart.objects.new_or_get(request)
#     # E o produto se adiciona a instância do campo M2M
#     cart_obj.products.add(product_obj) # cart_obj.products.add(product_id)
#     #cart_obj.products.remove(product_obj) # cart_obj.products.remove(product_id)
#     return redirect('produto_detalhe', id = product_id)
@require_POST
def cart_add(request,produto_id):
  carrinho = Carrinho(request)
  produto = get_object_or_404(Produto, id=produto_id)
  form = ProdutoAddCarrinhoForm(request.POST)
  if form.is_valid():
    cd=form.cleaned_data
    carrinho.add(produto=produto, quantity=cd['quantity'], override_quantity=cd['override'])
  return render(request,'carrinho.html')

def cart_remove(request, produto_id):
  carrinho = Carrinho(request)
  produto = get_object_or_404(Produto, id=produto_id)
  carrinho.remove(produto)
  return render(request,'carrinho.html')

##------> Home Page e debugger
def index(request):
  return render(request, 'index.html')
