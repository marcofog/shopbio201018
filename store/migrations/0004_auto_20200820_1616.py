# Generated by Django 3.1 on 2020-08-20 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200820_1555'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorie'},
        ),
        migrations.AlterField(
            model_name='prodotti',
            name='informazioni',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
