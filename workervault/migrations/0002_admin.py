# Generated by Django 4.1.13 on 2024-03-05 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workervault', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=' ', max_length=50)),
                ('password', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
