# Generated by Django 4.0.5 on 2022-07-28 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kcalculatorapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kcal',
            name='actv',
            field=models.FloatField(choices=[(1.2, '주1-2회 운동 | 좌식 생활'), (1.375, '주2-3회 운동 | 적은 활동'), (1.55, '주3-4회 운동 | 평균적 활동'), (1.6375, '주4-5회 운동 | 평균 ~ 많은 활동'), (1.725, '주5-6회 운동 | 많은 활동'), (1.9, '주7회 하루 2번운동 | 아주 많은활동')], default=1, max_length=200, verbose_name='활동량'),
            preserve_default=False,
        ),
    ]
