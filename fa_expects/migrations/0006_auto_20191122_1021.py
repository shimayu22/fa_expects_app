# Generated by Django 2.2.6 on 2019-11-22 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fa_expects', '0005_faexpects_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faexpects',
            name='priority',
            field=models.IntegerField(choices=[('', '選択'), (1, '第一希望'), (2, '第二希望'), (3, '第三希望'), (4, '第四希望以降')], default=0, verbose_name='優先度'),
        ),
    ]