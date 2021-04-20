# Generated by Django 3.1.5 on 2021-04-20 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countdown_core', '0005_auto_20210419_0020'),
        ('custom_user', '0005_auto_20210127_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bookmarked_countdowns',
            field=models.ManyToManyField(to='countdown_core.Countdown'),
        ),
    ]