from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, m2m_changed
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
  #Restringir a quantidade do produto por lista com kg, g, unidade, peça e etc....
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


REVIEW_NOTAS = [
  ('1','1'),
  ('2','2'),
  ('3','3'),
  ('4','4'),
  ('5','5')
]
class ProdutoReview(models.Model):
  produto_rating = models.ForeignKey(Produto, on_delete=models.CASCADE)
  usuario_rating = models.ForeignKey(User, on_delete=models.CASCADE)
  texto_avaliacao = models.TextField('avaliacao', max_length=500, null=True)
  nota_avaliacao = models.FloatField(null=True,choices=REVIEW_NOTAS)
  criado_em = models.DateTimeField(auto_now_add=True)

#---------------------Implementação do carrinho

class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id = cart_id)
        if qs.count == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user = request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user = None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user = user_obj)


class Cart(models.Model):
  user  = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
  products  = models.ManyToManyField(Produto, blank=True)
  total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
  subtotal = models.DecimalField(default = 0.00, max_digits=100, decimal_places = 2)
  updated = models.DateTimeField(auto_now=True)
  timestamp = models.DateTimeField(auto_now_add=True)

  objects= CartManager()

  def __str__(self):
    return str(self.id)

def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
  #print(action)
  if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
    #print(instance.products.all())
    #print(instance.total)
    products = instance.products.all()
    total = 0
    for product in products:
      total += product.preco_produto
    if instance.subtotal != total:
      instance.subtotal = total
      instance.save()
    #print(total)
    instance.subtotal = total
    instance.save()

m2m_changed.connect(m2m_changed_cart_receiver, sender = Cart.products.through)

def pre_save_cart_receiver(sender, instance, *args, **kwargs):
  instance.total = instance.subtotal + 10 # considere o 10 como uma taxa de entrega

pre_save.connect(pre_save_cart_receiver, sender = Cart)
