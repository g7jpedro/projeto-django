# Generated by Django 4.2.4 on 2023-09-18 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='porcao_tipo',
            field=models.CharField(max_length=20, verbose_name='Tipo de porção'),
        ),
    ]
