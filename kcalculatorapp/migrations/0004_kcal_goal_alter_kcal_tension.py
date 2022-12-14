# Generated by Django 4.0.5 on 2022-08-03 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kcalculatorapp', '0003_kcal_tension'),
    ]

    operations = [
        migrations.AddField(
            model_name='kcal',
            name='goal',
            field=models.CharField(choices=[('diet', '다이어트'), ('lean', '린매스')], default=1, max_length=200, verbose_name='운동목적'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kcal',
            name='tension',
            field=models.CharField(choices=[('low', '저강도'), ('mid', '중강도'), ('high', '고강도')], max_length=200, verbose_name='운동강도'),
        ),
    ]
