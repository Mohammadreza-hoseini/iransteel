# Generated by Django 3.2.5 on 2021-07-18 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0005_section2part1_section2part2_section2part3'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.PROTECT, to='auth.user'),
            preserve_default=False,
        ),
    ]
