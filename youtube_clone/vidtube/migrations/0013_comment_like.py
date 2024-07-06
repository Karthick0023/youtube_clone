# Generated by Django 4.2.6 on 2024-06-06 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidtube', '0012_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('vid_id', models.CharField(max_length=150)),
                ('comments', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('acc_id', models.CharField(max_length=150)),
            ],
        ),
    ]