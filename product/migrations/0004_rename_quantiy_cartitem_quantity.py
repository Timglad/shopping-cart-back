# Generated by Django 3.2.16 on 2023-02-21 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_archived'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='quantiy',
            new_name='quantity',
        ),
    ]
