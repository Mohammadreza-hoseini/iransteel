# Generated by Django 3.2.5 on 2021-07-19 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_auto_20210719_0728'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headerimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='backgroud/%Y/%m/%d/')),
            ],
        ),
    ]