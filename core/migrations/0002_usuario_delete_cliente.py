# Generated by Django 4.1 on 2022-08-23 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario', models.CharField(max_length=225, verbose_name='nome_usuario')),
                ('sobrenome_usuario', models.CharField(max_length=225, verbose_name='sobrenome_usuario')),
                ('email_usuario', models.CharField(max_length=225, verbose_name='email_usuario')),
                ('data_nascimento_usuario', models.DateField(blank=True, null=True, verbose_name='data_nascimento_usuario')),
                ('DOC_Usuario', models.CharField(max_length=225, verbose_name='DOC_Usuario')),
                ('is_CNPJ', models.BooleanField(verbose_name='is_CNPJ')),
                ('is_Produtor', models.BooleanField(verbose_name='is_Produtor')),
                ('senha_usuario', models.CharField(max_length=225, verbose_name='senha_usuario')),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
