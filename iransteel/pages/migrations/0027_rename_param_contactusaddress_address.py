# Generated by Django 3.2.5 on 2021-07-20 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0026_contactusaddress_contactusemail_contactusphone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactusaddress',
            old_name='param',
            new_name='address',
        ),
    ]