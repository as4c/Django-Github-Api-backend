# Generated by Django 4.1.5 on 2023-01-14 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heroapi', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Repository',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
