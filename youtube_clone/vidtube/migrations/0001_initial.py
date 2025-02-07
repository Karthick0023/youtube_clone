# Generated by Django 4.2.6 on 2023-12-28 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('cha_des', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='uploadmod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('video', models.FileField(upload_to='')),
                ('des', models.CharField(max_length=50)),
                ('thumbnail', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='')),
                ('des', models.CharField(max_length=50)),
                ('thumbnail', models.ImageField(upload_to='')),
            ],
        ),
    ]
