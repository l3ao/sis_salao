# Generated by Django 3.2.5 on 2021-08-15 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0002_auto_20210317_1200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servico',
            old_name='valor',
            new_name='preco',
        ),
    ]
