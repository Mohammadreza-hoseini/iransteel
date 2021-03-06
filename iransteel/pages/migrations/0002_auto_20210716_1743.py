# Generated by Django 3.2.5 on 2021-07-16 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=255)),
                ('param', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='section1/%Y/%m/%d/')),
            ],
        ),
        migrations.AlterField(
            model_name='header',
            name='param1',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='header',
            name='param2',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='header',
            name='param3',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='header',
            name='titel',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
