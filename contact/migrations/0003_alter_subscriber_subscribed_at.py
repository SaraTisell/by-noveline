# Generated by Django 4.2.11 on 2024-04-07 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contactmessage_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='subscribed_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
