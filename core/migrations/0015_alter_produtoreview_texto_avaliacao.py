# Generated by Django 4.1 on 2022-09-05 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_rename_reviewrating_produtoreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtoreview',
            name='texto_avaliacao',
            field=models.TextField(max_length=500, null=True, verbose_name='avaliacao'),
        ),
    ]
