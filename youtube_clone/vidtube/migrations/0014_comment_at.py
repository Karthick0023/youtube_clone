# Generated by Django 4.2.6 on 2024-07-01 14:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidtube', '0013_comment_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]