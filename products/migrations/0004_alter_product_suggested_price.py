# Generated by Django 5.1.2 on 2024-11-03 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_price_product_is_purchase_with_tax_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='suggested_price',
            field=models.IntegerField(default=0, verbose_name='Precio Sugerido sin IVA'),
        ),
    ]