# Generated by Django 3.2.5 on 2021-07-20 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0024_auto_20210719_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactustitel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param', models.TextField(max_length=555)),
            ],
        ),
    ]