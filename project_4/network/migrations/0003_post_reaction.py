# Generated by Django 3.2.3 on 2021-09-03 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reaction',
            field=models.IntegerField(default=0),
        ),
    ]
