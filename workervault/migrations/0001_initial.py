# Generated by Django 4.1.13 on 2024-01-25 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkerVaultModel',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('phoneno', models.BigIntegerField(null=True)),
                ('emailid', models.EmailField(default='', max_length=254)),
                ('address', models.CharField(default='', max_length=400)),
                ('gender', models.CharField(default='', max_length=100)),
                ('location', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
