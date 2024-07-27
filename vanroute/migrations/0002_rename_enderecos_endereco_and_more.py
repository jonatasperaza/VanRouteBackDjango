# Generated by Django 5.0.7 on 2024-07-27 04:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('vanroute', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Enderecos',
            new_name='Endereco',
        ),
        migrations.RenameModel(
            old_name='Motoristas',
            new_name='Motorista',
        ),
        migrations.CreateModel(
            name='Van',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=7, unique=True)),
                ('capacidade', models.PositiveIntegerField()),
                ('motorista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vanroute.motorista')),
            ],
            options={
                'verbose_name': 'Van',
                'verbose_name_plural': 'Vans',
            },
        ),
    ]