# Generated by Django 3.2.5 on 2021-07-16 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_section1_titel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section1Part1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Section1Part2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Section1Part3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='section1/%Y/%m/%d/')),
            ],
        ),
        migrations.DeleteModel(
            name='Section1',
        ),
    ]
