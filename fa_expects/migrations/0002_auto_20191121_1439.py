# Generated by Django 2.2.6 on 2019-11-21 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fa_expects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faexpects',
            options={'ordering': ['priority'], 'verbose_name': 'FA予想', 'verbose_name_plural': 'FA予想'},
        ),
    ]
