# Generated by Django 4.1.13 on 2024-02-22 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workervault', '0006_rename_userid_contactus_emailid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='emailid',
            new_name='userid',
        ),
    ]
