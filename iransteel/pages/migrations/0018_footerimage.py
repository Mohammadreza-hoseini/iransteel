# Generated by Django 3.2.5 on 2021-07-18 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_footerfax_footerphone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footerimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='footer/%Y/%m/%d/')),
            ],
        ),
    ]
