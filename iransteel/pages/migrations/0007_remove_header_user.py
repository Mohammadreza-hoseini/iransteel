# Generated by Django 3.2.5 on 2021-07-18 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_header_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='header',
            name='user',
        ),
    ]
