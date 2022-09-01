from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

#Ao apresentar tirar todos os null=True e recriar as db's

class Usuario_pequi(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  data_nascimento_usuario = models.DateField('data_nascimento_usuario', blank=True, null=True )
  DOC_Usuario = models.CharField('DOC_Usuario', max_length=225)
  is_CNPJ = models.BooleanField('is_CNPJ', null=True)
  is_Produtor = models.BooleanField('is_Produtor', null=True)

  def __str__(self):
    return self.user.username


PRODUTO_CHOICES = [
  ('alimento', 'Alimento'),
  ('bebidas', 'Bebida'),
  ('cosmetico', 'Cosmetico'),
  ('vestimenta', 'Vestimenta'),
  ('outros','Outros')
]

class Produto(models.Model):

  user_produtor = models.ForeignKey(User,default=None , null=True, on_delete=models.CASCADE)

  nome_produto = models.CharField('nome_produto', max_length=225, null=True)
  preco_produto = models.DecimalField('preco_produto', decimal_places=2, max_digits=15, null=True)
  descricao_produto = models.CharField('descricao_produto',max_length=225, blank=True, null=True )
  quantidade_produto = models.DecimalField('quantidade_produto',decimal_places=2, max_digits=15, null=True)
  imagem_produto = models.ImageField('imagem_produto', blank=True, null=True, upload_to="core")
  tipo_produto = models.CharField('tipo_produto', max_length=200,choices=PRODUTO_CHOICES, null=True)

  def __str__(self) -> str:
     return self.nome_produto
ESTADO_CHOICES = [
  ('AC','Acre'),
  ('AL','Alagoas'),
  ('AP','Amapá'),
  ('AM','Amazonas'),
  ('BA','Bahia'),
  ('CE','Ceará'),
  ('DF','Distrito Federal'),
  ('ES','Espírito Santo'),
  ('GO','Goiás'),
  ('MA','Maranhão'),
  ('MT','Mato Grosso'),
  ('MS','Mato Grosso do Sul'),
  ('MG','Minas Gerais'),
  ('PA','Pará'),
  ('PB','Paraíba'),
  ('PR','Paraná'),
  ('PE','Pernambuco'),
  ('PI','Piauí'),
  ('RJ','Rio de Janeiro'),
  ('RN','Rio Grande do Norte'),
  ('RS','Rio Grande do Sul'),
  ('RO','Rondônia'),
  ('RR','Roraima'),
  ('SC','Santa Catarina'),
  ('SP','São Paulo'),
  ('SE','Sergipe'),
  ('TO','Tocantins')
]
class Endereco(models.Model):
  user_endereco = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
  rua_endereco = models.CharField('rua_endereco', max_length=225, null=True)
  CEP_endereco = models.CharField('CEP_endereco', max_length=225, null=True)
  bairro_endereco = models.CharField('bairro_endereco', max_length=225, null=True)
  cidade_endereco = models.CharField('cidade_endereco', max_length=225, null=True)
  estado_endereco = models.CharField('estado_endereco', max_length=225,choices=ESTADO_CHOICES, null=True)


class Contato(models.Model):
  user_contato = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
  telefone_contato = models.CharField('telefone_contato',null=True, max_length=225)
  email_contato = models.CharField('email_contato',null=True, max_length=225)
  is_wpp = models.BooleanField('is_wpp', null=True)

