import django_filters
from django_filters import CharFilter
from .models import Produto

class ProdutoFilter(django_filters.FilterSet):
  nome_produto = CharFilter(field_name='nome_produto', lookup_expr='icontains')
  class Meta:
    model = Produto
    fields = ['nome_produto', 'preco_produto', 'tipo_produto']
