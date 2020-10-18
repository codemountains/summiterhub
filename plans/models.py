from django.db import models
from summiterhub import settings_core
import uuid
from utils import choices
from gears.models import Gear


class Plan(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	created_user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_created_user_id',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_updated_user_id',
		on_delete=models.CASCADE
	)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	purpose_type = models.IntegerField(choices=choices.PURPOSE_TYPE)
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
		return str(self.id)


class PlanCustomGear(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	created_user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_customGear_created_user_id',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_customGear_updated_user_id',
		on_delete=models.CASCADE
	)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	plan_id = models.ForeignKey(
		Gear,
		related_name='plan_customGear_gear_id',
		on_delete=models.CASCADE
	)
	name = models.CharField(max_length=50)
	sort_index = models.IntegerField()

	def __str__(self):
		return self.name


class PlanMountain(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	created_user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_mountain_created_user_id',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_mountain_updated_user_id',
		on_delete=models.CASCADE
	)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	plan_id = models.ForeignKey(
		Plan,
		related_name='plan_mountain_plan_id',
		on_delete=models.CASCADE
	)
	name = models.CharField(max_length=50)
	sort_index = models.IntegerField()

	def __str__(self):
		return self.name


class PlanRoute(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	created_user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_route_created_user_id',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_route_updated_user_id',
		on_delete=models.CASCADE
	)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	plan_id = models.ForeignKey(
		Plan,
		related_name='plan_route_plan_id',
		on_delete=models.CASCADE
	)
	plan_date = models.DateField()

	def __str__(self):
		return str(self.plan_date) + ' ' + str(self.plan_id)


class PlanRouteDetail(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	created_user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_route_detail_created_user_id',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_route_detail_updated_user_id',
		on_delete=models.CASCADE
	)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	plan_route_id = models.ForeignKey(
		PlanRoute,
		related_name='plan_route_detail_plan_route_id',
		on_delete=models.CASCADE
	)
	name = models.CharField(max_length=50)
	is_staying = models.BooleanField(default=False)
	sort_index = models.IntegerField()

	def __str__(self):
		return self.name


class PlanEscapeRoute(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	created_user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_escape_route_created_user_id',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_escape_route_updated_user_id',
		on_delete=models.CASCADE
	)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	plan_id = models.ForeignKey(
		Plan,
		related_name='plan_escape_route_plan_id',
		on_delete=models.CASCADE
	)
	content = models.TextField(max_length=300, blank=True, null=True)

	def __str__(self):
		return str(self.plan_id)


class PlanMember(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	created_user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_member_created_user_id',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_member_updated_user_id',
		on_delete=models.CASCADE
	)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	plan_id = models.ForeignKey(
		Plan,
		related_name='plan_member_plan_id',
		on_delete=models.CASCADE
	)
	user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_member_user_id',
		on_delete=models.SET_NULL,
		blank=True,
		null=True
	)
	name = models.CharField(max_length=100)
	postal_code = models.CharField(max_length=8)
	prefecture = models.IntegerField(choices=choices.PREFECTURE)
	address = models.CharField(max_length=200)
	gender_type = models.IntegerField(choices=choices.GENDER_TYPE)
	blood_type = models.IntegerField(choices=choices.BLOOD_TYPE)
	home_phone_number = models.CharField(max_length=13, blank=True, null=True)
	cell_phone_number = models.CharField(max_length=13, blank=True, null=True)
	emergency_contact_name = models.CharField(max_length=100)
	emergency_contact_phone = models.CharField(max_length=13)
	emergency_contact_email = models.CharField(max_length=100, blank=True, null=True)
	insurance_name = models.CharField(max_length=100, blank=True, null=True)
	insurance_number = models.CharField(max_length=100, blank=True, null=True)
	hitococo_id = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.name


class Bookmark(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	user_id = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='bookmark_user_id',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	plan_id = models.ForeignKey(
		Plan,
		related_name='bookmark_plan_id',
		on_delete=models.CASCADE
	)

	def __str__(self):
		return str(self.plan_id)
