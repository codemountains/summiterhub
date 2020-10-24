# Generated by Django 3.1.2 on 2020-10-24 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='readnews',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='read_news_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='readnews',
            unique_together={('user_id', 'news_id')},
        ),
    ]
