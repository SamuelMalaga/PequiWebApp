from django.db import models
import uuid

# Create your models here.

# class Produto(models,Model):
#   nome_produto = models.CharField('nome_produto', max_length=225)
#   preco_produto = models.DecimalField('preco_produto', decimal_places=2, max_digits=15)
#   descricao_produto = models.CharField('descricao_produto', blank=True, null=True )
#   quantidade_produto = models.DecimalField('quantidade_produto')
#   imagem_produto = models.ImageField('imagem_produto', blank=True, null=True, upload_to="core")
#   tipo_produto = models.CharField('tipo_produto', max_length=200)
#   produtor_id = models.ForeignKey('Produtor', on_delete=models.CASCADE)

class Usuario(models.Model):
  nome_usuario = models.CharField('nome_usuario', max_length=225)
  sobrenome_usuario = models.CharField('sobrenome_usuario', max_length=225)
  email_usuario = models.CharField('email_usuario', max_length=225)
  data_nascimento_usuario = models.DateField('data_nascimento_usuario', blank=True, null=True )
  DOC_Usuario = models.CharField('DOC_Usuario', max_length=225)
  is_CNPJ = models.BooleanField('is_CNPJ')
  is_Produtor = models.BooleanField('is_Produtor')
  senha_usuario = models.CharField('senha_usuario', max_length=225)

  def __str__(self) -> str:
    return self.nome_usuario

class Produto(models.Model):
  nome_produto = models.CharField('nome_produto', max_length=225)
  preco_produto = models.DecimalField('preco_produto', decimal_places=2, max_digits=15)
  descricao_produto = models.CharField('descricao_produto',max_length=225, blank=True, null=True )
  quantidade_produto = models.DecimalField('quantidade_produto',decimal_places=2, max_digits=15)
  imagem_produto = models.ImageField('imagem_produto', blank=True, null=True, upload_to="core")
  tipo_produto = models.CharField('tipo_produto', max_length=200)
  def __str__(self) -> str:
    return self.nome_produto

class Endereco(models.Model):
  rua_endereco = models.CharField('rua_endereco', max_length=225)
  CEP_endereco = models.CharField('CEP_endereco', max_length=225)
  bairro_endereco = models.CharField('bairro_endereco', max_length=225)
  cidade_endereco = models.CharField('cidade_endereco', max_length=225)
  estado_endereco = models.CharField('estado_endereco', max_length=225)

  #def __str__(self) -> str:
  #  return self.nome_produto

class Contato(models.Model):
  telefone_contato = models.CharField('telefone_contato', max_length=225)
  email_contato = models.CharField('email_contato', max_length=225)
  is_wpp = models.BooleanField('is_wpp')

  #def __str__(self) -> str:
  #  return self.nome_produto
