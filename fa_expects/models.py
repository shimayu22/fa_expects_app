from django.db import models
from django.core import validators

# Create your models here.
class Players(models.Model):

    POSITION_CHOICES = (
        ('', '選択'),
        (1, '投'),
        (2, '捕'),
        (3, '一'),
        (4, '二'),
        (5, '三'),
        (6, '遊'),
        (7, '外'),
    )

    DOMINANT_HAND_CHOICES = (
        ('', '選択'),
        (1, '右投右打'),
        (2, '右投左打'),
        (3, '右投両打'),
        (4, '左投左打'),
    )

    NPB_TEAM_CHOICES = (
        ('', '選択'),
        ('1', '西武'),
        ('2', 'ソフトバンク'),
        ('3', '楽天'),
        ('4', 'ロッテ'),
        ('5', '日本ハム'),
        ('6', 'オリックス'),
        ('7', '巨人'),
        ('8', 'DeNA'),
        ('9', '阪神'),
        ('10', '広島'),
        ('11', '中日'),
        ('12', 'ヤクルト'),
    )

    name = models.CharField(
        verbose_name="選手名",
        max_length=10,
    )

    age = models.PositiveSmallIntegerField(
        verbose_name="年齢",
        validators=[validators.MinValueValidator(26),validators.MaxValueValidator(60)],
    )

    position = models.IntegerField(
        verbose_name="メインポジション",
        choices=POSITION_CHOICES,
        default=0,
    )

    dominant_hand = models.IntegerField(
        verbose_name="利き手",
        choices=DOMINANT_HAND_CHOICES,
        default=0,
    )

    department = models.IntegerField(
        verbose_name="現所属球団",
        choices=NPB_TEAM_CHOICES,
        default=0,
    )

    created_at = models.DateTimeField(
        verbose_name="登録日",
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.name} : {self.POSITION_CHOICES[self.position]} : {self.NPB_TEAM_CHOICES[self.department]}'

    class Meta:
        verbose_name = "選手情報"
        verbose_name_plural = "選手情報"
        ordering = ['department', 'position']


class FaExpects(models.Model):

    PRIORITY_CHOICES = (
        ('', '選択'),
        ('1', '第一希望'),
        ('2', '第二希望'),
        ('3', '第三希望'),
        ('4', '第四希望以降'),
    )

    player_id = models.ForeignKey(
        Players,
        on_delete=models.CASCADE,
        verbose_name="選手",
    )

    priority = models.IntegerField(
        verbose_name="優先度",
        choices=PRIORITY_CHOICES,
        default=0,
    )

    created_at = models.DateTimeField(
        verbose_name="登録日",
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.player_id} : {self.PRIORITY_CHOICES[self.priority]}'

    class Meta:
        verbose_name = "FA予想"
        verbose_name_plural = "FA予想"
        ordering = ['priority']