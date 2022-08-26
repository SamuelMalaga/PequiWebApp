from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Usuario_pequi(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  data_nascimento_usuario = models.DateField('data_nascimento_usuario', blank=True, null=True )
  DOC_Usuario = models.CharField('DOC_Usuario', max_length=225)
  is_CNPJ = models.BooleanField('is_CNPJ', null=True)
  is_Produtor = models.BooleanField('is_Produtor', null=True)

  def __str__(self):
    return self.user.username


class Produto(models.Model):

  ID_User_Produtor_Produto = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

  nome_produto = models.CharField('nome_produto', max_length=225, null=True)
  preco_produto = models.DecimalField('preco_produto', decimal_places=2, max_digits=15, null=True)
  descricao_produto = models.CharField('descricao_produto',max_length=225, blank=True, null=True )
  quantidade_produto = models.DecimalField('quantidade_produto',decimal_places=2, max_digits=15, null=True)
  imagem_produto = models.ImageField('imagem_produto', blank=True, null=True, upload_to="core")
  tipo_produto = models.CharField('tipo_produto', max_length=200, null=True)

  def __str__(self) -> str:
     return self.nome_produto

class Endereco(models.Model):
  # rua_endereco = models.CharField('rua_endereco', max_length=225)
  # CEP_endereco = models.CharField('CEP_endereco', max_length=225)
  # bairro_endereco = models.CharField('bairro_endereco', max_length=225)
  # cidade_endereco = models.CharField('cidade_endereco', max_length=225)
  # estado_endereco = models.CharField('estado_endereco', max_length=225)
  # ID_usuario_endereco = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE)

  #def __str__(self) -> str:
  #  return self.nome_produto
  pass
class Contato(models.Model):
  # telefone_contato = models.CharField('telefone_contato', max_length=225)
  # email_contato = models.CharField('email_contato', max_length=225)
  # is_wpp = models.BooleanField('is_wpp')
  # ID_usuario_contato = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE)

  #def __str__(self) -> str:
  #  return self.nome_produto
  pass
