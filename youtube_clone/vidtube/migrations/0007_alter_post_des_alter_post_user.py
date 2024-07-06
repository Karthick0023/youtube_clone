# Generated by Django 4.2.6 on 2024-01-05 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vidtube', '0006_alter_post_options_alter_account_dp_alter_post_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='des',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vidtube.account'),
        ),
    ]