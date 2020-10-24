# Generated by Django 3.1.2 on 2020-10-24 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plans', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='planroutedetail',
            name='created_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_route_detail_created_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='planroutedetail',
            name='plan_route_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_route_detail_plan_route_id', to='plans.planroute'),
        ),
        migrations.AddField(
            model_name='planroutedetail',
            name='updated_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_route_detail_updated_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='planroute',
            name='created_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_route_created_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='planroute',
            name='plan_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_route_plan_id', to='plans.plan'),
        ),
        migrations.AddField(
            model_name='planroute',
            name='updated_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_route_updated_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='planmember',
            name='created_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_member_created_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='planmember',
            name='plan_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_member_plan_id', to='plans.plan'),
        ),
        migrations.AddField(
            model_name='planmember',
            name='updated_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_member_updated_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='planmember',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plan_member_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='plangear',
            name='created_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_gear_created_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='plangear',
            name='plan_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='plan_gear_plan_id', to='plans.plan'),
        ),
        migrations.AddField(
            model_name='plangear',
            name='updated_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_gear_updated_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='planescaperoute',
            name='created_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_escape_route_created_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='planescaperoute',
            name='plan_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='plan_escape_route_plan_id', to='plans.plan'),
        ),
        migrations.AddField(
            model_name='planescaperoute',
            name='updated_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_escape_route_updated_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='plancustomgear',
            name='created_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_custom_gear_created_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='plancustomgear',
            name='plan_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_custom_gear_plan_id', to='plans.plan'),
        ),
        migrations.AddField(
            model_name='plancustomgear',
            name='updated_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_custom_gear_updated_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='plan',
            name='created_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_created_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='plan',
            name='updated_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_updated_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='plan_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmark_plan_id', to='plans.plan'),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmark_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='bookmark',
            unique_together={('user_id', 'plan_id')},
        ),
    ]