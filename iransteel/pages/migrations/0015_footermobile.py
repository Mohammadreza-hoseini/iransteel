# Generated by Django 3.2.5 on 2021-07-18 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_footeraddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footermobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=255)),
            ],
        ),
    ]