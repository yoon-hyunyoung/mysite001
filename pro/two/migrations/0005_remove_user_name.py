# Generated by Django 3.1.5 on 2021-03-15 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('two', '0004_auto_20210315_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
