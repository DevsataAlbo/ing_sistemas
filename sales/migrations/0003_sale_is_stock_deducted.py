# Generated by Django 5.1.2 on 2024-11-08 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_alter_sale_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='is_stock_deducted',
            field=models.BooleanField(default=False, verbose_name='Stock descontado'),
        ),
    ]