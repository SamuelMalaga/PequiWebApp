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
from core.views import index, login_user, login_submit, registre, create_usuario, logout_user, produto,produto_submit, cadastro_endereco, endereco_submit, cadastro_contato, contato_submit
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('login/submit/', login_submit, name='login_submit'),
    path('registre/', registre, name='registre'),
    path('registre/submit/', create_usuario, name='create_usuario'),
    path('produto/', produto, name='produto'),
    path('produto/submit', produto_submit, name='produto_submit'),
    path('endereco/', cadastro_endereco, name='cadastro_endereco'),
    path('endereco/submit', endereco_submit, name='endereco_submit'),
    path('contato/', cadastro_contato, name='cadastro_contato'),
    path('contato/submit', contato_submit, name='contato_submit')


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

