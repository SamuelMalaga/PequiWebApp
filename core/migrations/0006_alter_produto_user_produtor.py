# Generated by Django 4.1 on 2022-08-26 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_rename_id_user_produtor_produto_user_produtor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='user_produtor',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
