# Generated by Django 4.1.1 on 2022-09-24 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_orders_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pictures',
            new_name='Picture',
        ),
    ]
