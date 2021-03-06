# Generated by Django 3.2.5 on 2021-07-19 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_alter_aboutus_param'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footeraddress',
            name='address',
            field=models.TextField(max_length=555),
        ),
        migrations.AlterField(
            model_name='footerparamsright',
            name='param',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='footertitel',
            name='titel',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='footertitelleft',
            name='titel',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='footertitelright',
            name='titel',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='headerparam',
            name='param',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='headertitel',
            name='titel',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='section1part1',
            name='titel',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='section1part2',
            name='param',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='section2part1',
            name='titel',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='section2part2',
            name='param',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='section3part1',
            name='titel',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='section3part2',
            name='param',
            field=models.TextField(max_length=255),
        ),
    ]
