
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Endereco, Usuario_pequi, Produto, Contato, ProdutoReview



#---->Formulários para criação de usuário pequi, classe base de Usuário do django e atributos estendidos
class ExtendedUserCreationForms(UserCreationForm):
  email = forms.EmailField(required=True)
  first_name = forms.CharField(max_length=50, required=True)
  last_name = forms.CharField(max_length=150)

  class Meta:
    model = User
    fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control form-control-sm ', 'value' : "Cadastrar", 'label': "Cadastrar"}),
        'email': forms.TextInput(attrs={'class': 'form-control form-control-sm '}),
        'first_name': forms.TextInput(attrs={'class': 'form-control form-control-sm '}),
        'last_name': forms.TextInput(attrs={'class': 'form-control form-control-sm '}),
        'password1': forms.TextInput(attrs={'class': 'form-control form-control-sm '}),
        'password2': forms.TextInput(attrs={'class': 'form-control form-control-sm '}),


    }
    def save(self, commit=True):
      user = super().save(commit=False)

      user.email = self.cleaned_data['email']
      user.first_name = self.cleaned_data['first_name']
      user.last_name = self.cleaned_data['last_name']

      if commit:
        user.save()
      return user


class UserPequiForm(forms.ModelForm):
  class Meta:
    model = Usuario_pequi
    fields = ('data_nascimento_usuario', 'DOC_Usuario', 'is_CNPJ', 'is_Produtor')


#------->Formulários para atualização de dados cadastrais
class AtualizacaoCadastroForm(UserChangeForm):
  class Meta:
    model = User
    fields = ('first_name', 'last_name','username', 'email' )

class AtualizacaoUserPequi(forms.ModelForm):
  class Meta:
    model = Usuario_pequi
    fields = ('data_nascimento_usuario', 'DOC_Usuario', 'is_CNPJ', 'is_Produtor')

#----->Forms para o cadastro de produtos
##------> Ajustar o tipo de produto para dropdown
class ProdutoModelForm(forms.ModelForm):

  class Meta:
    model = Produto
    fields = ['nome_produto', 'preco_produto', 'descricao_produto', 'quantidade_produto', 'imagem_produto', 'tipo_produto']

#----->Forms para o cadastro de enderecos
class EnderecoModelForm(forms.ModelForm):
  class Meta:
    model = Endereco
    fields = ['rua_endereco','CEP_endereco', 'bairro_endereco', 'cidade_endereco', 'estado_endereco' ]

#-----> Forms para o cadastro de contato
class ContatoModelForm(forms.ModelForm):
  class Meta:
    model = Contato
    fields = ['telefone_contato','email_contato', 'is_wpp']

#------> Forms para o registro do produto
class ReviewForms(forms.ModelForm):
  class Meta:
    model = ProdutoReview
    fields = ['texto_avaliacao', 'nota_avaliacao']


#-------> Forms para adição de produtos no carrinho
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,21)]
class ProdutoAddCarrinhoForm(forms.Form):
  quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
  override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

