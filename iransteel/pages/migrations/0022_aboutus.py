# Generated by Django 3.2.5 on 2021-07-19 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_headerimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='aboutus/%Y/%m/%d/')),
                ('param', models.CharField(max_length=5555)),
            ],
        ),
    ]
