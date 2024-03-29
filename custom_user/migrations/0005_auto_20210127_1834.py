# Generated by Django 3.1.5 on 2021-01-27 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0004_auto_20210127_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
    ]
