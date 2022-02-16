# Generated by Django 4.0.2 on 2022-02-15 22:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last login:'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_request',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Last request:'),
        ),
    ]