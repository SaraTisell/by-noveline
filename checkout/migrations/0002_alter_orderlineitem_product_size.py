# Generated by Django 4.2.11 on 2024-04-04 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='product_size',
            field=models.CharField(max_length=12),
        ),
    ]
