# Generated by Django 3.1.5 on 2021-04-22 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countdown_core', '0007_reactionset'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countdown',
            name='cry_reaction',
        ),
        migrations.RemoveField(
            model_name='countdown',
            name='laugh_reaction',
        ),
        migrations.RemoveField(
            model_name='countdown',
            name='like_reaction',
        ),
        migrations.RemoveField(
            model_name='countdown',
            name='negative_reaction',
        ),
    ]