# Generated by Django 3.2.3 on 2021-09-21 13:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_auto_20210904_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='reaction',
        ),
        migrations.AddField(
            model_name='post',
            name='reaction',
            field=models.ManyToManyField(related_name='Liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='follower',
            field=models.ManyToManyField(related_name='Profile_follower', to=settings.AUTH_USER_MODEL),
        ),
    ]
