# Generated by Django 4.1 on 2022-08-25 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_alter_usuario_pequi_is_cnpj_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='ID_User_Produtor_Produto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='produto',
            name='descricao_produto',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='descricao_produto'),
        ),
        migrations.AddField(
            model_name='produto',
            name='imagem_produto',
            field=models.ImageField(blank=True, null=True, upload_to='core', verbose_name='imagem_produto'),
        ),
        migrations.AddField(
            model_name='produto',
            name='nome_produto',
            field=models.CharField(max_length=225, null=True, verbose_name='nome_produto'),
        ),
        migrations.AddField(
            model_name='produto',
            name='preco_produto',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True, verbose_name='preco_produto'),
        ),
        migrations.AddField(
            model_name='produto',
            name='quantidade_produto',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True, verbose_name='quantidade_produto'),
        ),
        migrations.AddField(
            model_name='produto',
            name='tipo_produto',
            field=models.CharField(max_length=200, null=True, verbose_name='tipo_produto'),
        ),
    ]