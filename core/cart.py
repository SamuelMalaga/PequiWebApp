from decimal import Decimal

from django.conf import settings

from core.models import Produto


class Carrinho(object):

  def __init__(self, request):
    """Inicializando o carrinho"""
    self.session=request.session
    cart = self.session.get(settings.CART_SESSION_ID)
    if not cart:
      cart=self.session[settings.CART_SESSION_ID]={}
    self.cart=cart


  def add(self, produto, quantity=1, override_quantity=False):
    produto_id = str(produto.id)
    if produto_id not in self.cart:
      self.cart[produto_id]={'quantity': 0, 'price': str(produto.preco_produto)}

    if override_quantity:
      self.cart[produto_id]['quantity']=quantity
    else:
      self.cart[produto_id]['quantity'] += quantity
    self.save()

  def save(self):
    self.session.modified = True


  def remove(self, produto):
    produto_id = str(produto.id)
    if produto_id in self.cart:
      del self.cart[produto_id]
      self.save()

  def __iter__(self):
    produto_ids = self.cart.keys()
    produtos = Produto.objects.filter(id__in=produto_ids)

    cart = self.cart.copy()
    for produto in produtos:
      cart[str(produto.id)]['product'] = produto

    for item in cart.values():
      item['price']=Decimal(item['price'])
      item['total_price']=item['price'] * item['quantity']
      yield item

  def __len__(self):
    return sum(item['quantity'] for item in self.cart.values())

  def get_total_price(self):
    return sum(Decimal(item['price'] * item['quantity'] for item in self.cart.values()))

  def clear(self):
    del self.session[settings.CART_SESSION_ID]
    self.save()
