# Generated by Django 3.1.7 on 2021-02-24 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Polo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polo', models.CharField(max_length=60, verbose_name='Polo')),
                ('endereco', models.CharField(max_length=150, verbose_name='Endereço')),
                ('telefone', models.CharField(max_length=17, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'Polo',
                'ordering': ['polo'],
            },
        ),
    ]
