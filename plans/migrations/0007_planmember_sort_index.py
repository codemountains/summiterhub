# Generated by Django 3.1.2 on 2020-11-23 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0006_auto_20201123_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='planmember',
            name='sort_index',
            field=models.IntegerField(null=True),
        ),
    ]