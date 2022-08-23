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

class Cliente(models.Model):
  nome_cliente = models.CharField('nome_cliente', max_length=225)
  sobrenome_cliente = models.CharField('sobrenome_cliente', max_length=225)
  email_cliente = models.DecimalField('email_cliente', max_length=225)
  data_nascimento_cliente = models.DateField('data_nascimento_cliente', blank=True, null=True )
  CPF_cliente = models.CharField('CPF_cliente', max_length=225)
  is_Produtor = models.BooleanField('is_Produtor')
  tipo_produto = models.CharField('tipo_produto', max_length=200)
  produtor_id = models.ForeignKey('Produtor', on_delete=models.CASCADE)


