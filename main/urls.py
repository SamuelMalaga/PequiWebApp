"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import (
                        index, login_user, login_submit,
                        registre,create_usuario, logout_user,
                        produto,produto_submit, cadastro_endereco,
                        endereco_submit, cadastro_contato,
                        contato_submit, produto_detalhe, ajuda,
                        sobre, minha_conta, submit_review,
                        alterar_dados_conta, alterar_dados_produto, remover_produto,
                        pagina_produtos
                        )
from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'

urlpatterns = [
    #pagina admin
    path('admin/', admin.site.urls),

    #Página inicial
    path('', index, name='pagina_inicial'),

    #Página Produtos
    path('produtos/', pagina_produtos, name='pagina_produtos'),

    #Login e logout
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('login/submit/', login_submit, name='login_submit'),

    #Cadastro
    path('registre/', registre, name='registre'),
    path('registre/submit/', create_usuario, name='create_usuario'),

    #Criar produto
    path('produto/', produto, name='produto'),
    path('produto/submit', produto_submit, name='produto_submit'),

    #Página do produto e avaliação do produto
    path('produto/<int:id>', produto_detalhe, name='produto_detalhe'),
    path('submit_review/<int:id>/', submit_review, name='submit_review'),

    #Cadastrar endereco
    path('endereco/', cadastro_endereco, name='cadastro_endereco'),
    path('endereco/submit', endereco_submit, name='endereco_submit'),

    #Cadastrar contato
    path('contato/', cadastro_contato, name='cadastro_contato'),
    path('contato/submit', contato_submit, name='contato_submit'),

    #Página de ajuda
    path('ajuda/', ajuda, name='ajuda'),

    #Minha Conta
    path('usuario/<int:id>', minha_conta, name='minha_conta'),

    #Alterar dados do cadastro
    path('editar_cadastro/', alterar_dados_conta, name='alterar_dados_conta'),

    #Alterar dados do produto
    path('editar_produto/<int:produto_id>', alterar_dados_produto, name='alterar_dados_produto'),

    #Remover Produto
    path('remover_produto/<int:produto_id>', remover_produto, name='remover_produto'),

    #Sobre nós
    path('sobre/', sobre, name='sobre')


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

