# Generated by Django 3.2.16 on 2023-02-21 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
