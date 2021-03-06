# Generated by Django 3.2.5 on 2021-07-16 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20210716_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section2Part1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Section2Part2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Section2Part3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='section2/%Y/%m/%d/')),
            ],
        ),
    ]
