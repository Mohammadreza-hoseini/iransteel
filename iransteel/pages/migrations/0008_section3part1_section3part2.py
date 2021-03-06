# Generated by Django 3.2.5 on 2021-07-18 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_remove_header_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section3Part1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Section3Part2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='section3/%Y/%m/%d/')),
                ('param', models.CharField(max_length=255)),
            ],
        ),
    ]
