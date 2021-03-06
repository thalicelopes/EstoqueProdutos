# Generated by Django 4.0.4 on 2022-05-11 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor', models.CharField(max_length=200, verbose_name='Cor')),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=200, verbose_name='Produto')),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Preço')),
                ('quantidade', models.IntegerField(default=0, verbose_name='Quantidade')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateTimeField(auto_now_add=True, verbose_name='Modificado')),
                ('cor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='produto.cores', verbose_name='Cor')),
            ],
        ),
    ]
