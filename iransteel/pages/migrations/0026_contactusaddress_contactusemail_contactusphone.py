# Generated by Django 3.2.5 on 2021-07-20 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0025_contactustitel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactusaddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contactusemail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(max_length=555)),
            ],
        ),
        migrations.CreateModel(
            name='Contactusphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255)),
            ],
        ),
    ]
