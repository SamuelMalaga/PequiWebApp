from django.contrib import admin

from .models import Usuario_pequi,Produto, Endereco, Contato, ProdutoReview,Cart

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
  #list_display = ['nome_usuario', 'sobrenome_usuario', 'email_usuario', 'data_nascimento_usuario', 'DOC_Usuario', 'is_CNPJ', 'is_Produtor', 'senha_usuario']
  pass

class ProdutoAdmin(admin.ModelAdmin):
  list_display = ['user_produtor','nome_produto', 'preco_produto', 'descricao_produto','quantidade_produto','imagem_produto','tipo_produto']


class EnderecoAdmin(admin.ModelAdmin):
  list_display = ['rua_endereco', 'CEP_endereco', 'bairro_endereco', 'cidade_endereco', 'estado_endereco']


class ContatoAdmin(admin.ModelAdmin):
  list_display = ['telefone_contato', 'email_contato', 'is_wpp']
  pass

class ReviewAdmin(admin.ModelAdmin):
  list_display = ['produto_rating', 'usuario_rating', 'texto_avaliacao', 'nota_avaliacao', 'criado_em']
  pass


admin.site.register(Usuario_pequi, UsuarioAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(ProdutoReview, ReviewAdmin)
admin.site.register(Cart)

