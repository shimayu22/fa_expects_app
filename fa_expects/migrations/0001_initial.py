# Generated by Django 2.2.6 on 2019-11-21 05:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='選手名')),
                ('age', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(26), django.core.validators.MaxValueValidator(60)], verbose_name='年齢')),
                ('position', models.IntegerField(choices=[('', '選択'), (1, '投'), (2, '捕'), (3, '一'), (4, '二'), (5, '三'), (6, '遊'), (7, '外')], default=0, verbose_name='メインポジション')),
                ('dominant_hand', models.IntegerField(choices=[('', '選択'), (1, '右投右打'), (2, '右投左打'), (3, '右投両打'), (4, '左投左打')], default=0, verbose_name='利き手')),
                ('department', models.IntegerField(choices=[('', '選択'), ('1', '西武'), ('2', 'ソフトバンク'), ('3', '楽天'), ('4', 'ロッテ'), ('5', '日本ハム'), ('6', 'オリックス'), ('7', '巨人'), ('8', 'DeNA'), ('9', '阪神'), ('10', '広島'), ('11', '中日'), ('12', 'ヤクルト')], default=0, verbose_name='現所属球団')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
            ],
            options={
                'verbose_name': '選手情報',
                'verbose_name_plural': '選手情報',
                'ordering': ['department', 'position'],
            },
        ),
        migrations.CreateModel(
            name='FaExpects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(choices=[('', '選択'), ('1', '第一希望'), ('2', '第二希望'), ('3', '第三希望'), ('4', '第四希望以降')], default=0, verbose_name='優先度')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fa_expects.Players', verbose_name='選手')),
            ],
        ),
    ]