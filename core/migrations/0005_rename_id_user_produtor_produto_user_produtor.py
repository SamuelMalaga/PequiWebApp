# Generated by Django 4.1 on 2022-08-26 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_id_user_produtor_produto_produto_id_user_produtor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='id_user_produtor',
            new_name='user_produtor',
        ),
    ]
