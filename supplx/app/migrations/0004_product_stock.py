# Generated by Django 5.1.4 on 2025-02-25 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_buy'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
