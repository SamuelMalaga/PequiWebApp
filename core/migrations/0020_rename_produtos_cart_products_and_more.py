# Generated by Django 4.1 on 2022-09-11 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_rename_profile_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='produtos',
            new_name='products',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='usuario',
            new_name='user',
        ),
    ]
