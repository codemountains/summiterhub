from django.db import models
from summiterhub import settings_core
import uuid
from utils import choices


class Gear(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='gear_user_id',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	title = models.CharField(max_length=50)
	purpose_type = models.IntegerField(choices=choices.PURPOSE_TYPE)
	remarks = models.CharField(max_length=100, blank=True, null=True)
	has_rain_wear = models.BooleanField(default=True)
	has_winter_clothing = models.BooleanField(default=True)
	has_map = models.BooleanField(default=True)
	has_compass = models.BooleanField(default=True)
	has_headlamp = models.BooleanField(default=True)
	has_mobile_phone = models.BooleanField(default=True)
	has_spare_battery = models.BooleanField(default=True)
	has_first_aid_kit = models.BooleanField(default=True)
	has_emergency_tent = models.BooleanField(default=True)
	has_transceiver = models.BooleanField(default=False)
	call_sign = models.CharField(max_length=50, blank=True, null=True)
	has_radio = models.BooleanField(default=False)
	has_tent = models.BooleanField(default=False)
	has_sleeping_bag = models.BooleanField(default=False)
	has_stove = models.BooleanField(default=False)
	has_helmet = models.BooleanField(default=False)
	has_climbing_rope = models.BooleanField(default=False)
	has_climbing_gear = models.BooleanField(default=False)
	has_crampons = models.BooleanField(default=False)
	has_ice_axe = models.BooleanField(default=False)
	has_shovel = models.BooleanField(default=False)
	has_beacon = models.BooleanField(default=False)
	has_probe = models.BooleanField(default=False)
	has_snow_saw = models.BooleanField(default=False)
	has_riding_gear = models.BooleanField(default=False)
	riding_type = models.IntegerField(choices=choices.RIDING_TYPE, blank=True, null=True)

	def __str__(self):
		return self.title


class CustomGear(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='custom_gear_user_id',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	gear_id = models.ForeignKey(
		Gear,
		related_name='custom_gear_gear_id',
		on_delete=models.CASCADE
	)
	name = models.CharField(max_length=50)
	sort_index = models.IntegerField()

	def __str__(self):
		return self.name + '(' + str(self.gear_id) + ')'
