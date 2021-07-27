# Generated by Django 3.2.5 on 2021-07-21 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0029_contactusform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productsbackground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Productsimg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Productsparam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param', models.TextField(max_length=10000)),
            ],
        ),
    ]