# Generated by Django 4.2.3 on 2023-07-07 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_vendor'),
        ('cartsystem', '0005_alter_cart_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='inventory.product'),
        ),
    ]
