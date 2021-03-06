# Generated by Django 3.1.2 on 2020-10-27 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gears', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gear',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gear_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customgear',
            name='gear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_gear_gear', to='gears.gear'),
        ),
        migrations.AddField(
            model_name='customgear',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_gear_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
