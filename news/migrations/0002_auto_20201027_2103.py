# Generated by Django 3.1.2 on 2020-10-27 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='readnews',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='read_news_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='readnews',
            unique_together={('user', 'news')},
        ),
    ]
