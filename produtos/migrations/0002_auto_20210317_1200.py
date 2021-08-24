# Generated by Django 3.1.7 on 2021-03-17 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UnidMedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='qtde',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='produto',
            name='valorpago',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AddField(
            model_name='produto',
            name='valorvenda',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produtos.categoria'),
        ),
        migrations.AddField(
            model_name='produto',
            name='und_medida',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produtos.unidmedida'),
        ),
    ]
