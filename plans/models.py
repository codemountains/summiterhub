from django.db import models
from summiterhub import settings_core
import uuid
from utils import choices


class Plan(models.Model):
	"""
	登山計画モデル
	"""
	PURPOSE_TYPE = choices.PURPOSE_TYPE
	PREFECTURE = choices.PREFECTURE

	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	created_user = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_created_user',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_user = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_updated_user',
		on_delete=models.CASCADE
	)
	updated_at = models.DateTimeField(auto_now=True)
	purpose_type = models.IntegerField(choices=PURPOSE_TYPE)
	prefecture = models.IntegerField(choices=PREFECTURE)
	mountain_first = models.CharField(max_length=50)
	mountain_second = models.CharField(max_length=50, blank=True, null=True)
	mountain_third = models.CharField(max_length=50, blank=True, null=True)
	mountain_fourth = models.CharField(max_length=50, blank=True, null=True)
	mountain_fifth = models.CharField(max_length=50, blank=True, null=True)
	is_submitted = models.BooleanField(default=False)
	submitted_date = models.DateField(blank=True, null=True)
	entering_date = models.DateField(blank=False, null=False)
	descending_date = models.DateField(blank=False, null=False)
	affiliate_group_name = models.CharField(max_length=100, blank=True, null=True)
	affiliate_group_phone = models.CharField(max_length=13, blank=True, null=True)
	has_trail_snacks = models.BooleanField(default=True)
	water_liters = models.IntegerField()
	food_times = models.IntegerField()
	emergency_food_times = models.IntegerField()

	def __str__(self):
		return 'User: ' + str(self.created_user) + \
			' Enter: ' + str(self.entering_date) + \
			' Mountain: ' + self.mountain_first


class PlanGear(models.Model):
	"""
	登山計画装備モデル
	登山計画に対して装備を登録可能
	"""
	RIDING_TYPE = choices.RIDING_TYPE

	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	created_user = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_gear_created_user',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_user = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_gear_updated_user',
		on_delete=models.CASCADE
	)
	updated_at = models.DateTimeField(auto_now=True)
	plan = models.OneToOneField(
		Plan,
		related_name='plan_gear_plan',
		on_delete=models.CASCADE
	)
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
	riding_type = models.IntegerField(choices=RIDING_TYPE, blank=True, null=True)

	def __str__(self):
		return str(self.plan)


class PlanCustomGear(models.Model):
	"""
	登山計画カスタム装備モデル
	登山計画に対してカスタム装備を登録可能
	"""
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	created_user = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_custom_gear_created_user',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_user = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_custom_gear_updated_user',
		on_delete=models.CASCADE
	)
	updated_at = models.DateTimeField(auto_now=True)
	plan = models.ForeignKey(
		Plan,
		related_name='plan_custom_gear_plan',
		on_delete=models.CASCADE
	)
	name = models.CharField(max_length=50)
	sort_index = models.IntegerField()

	def __str__(self):
		return str(self.plan) + ' Name: ' + str(self.name)


class PlanRoute(models.Model):
	"""
	登山計画ルートモデル
	登山計画に対してルートを登録可能
	"""
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	created_user = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_route_created_user',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_user = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_route_updated_user',
		on_delete=models.CASCADE
	)
	updated_at = models.DateTimeField(auto_now=True)
	plan = models.ForeignKey(
		Plan,
		related_name='plan_route_plan',
		on_delete=models.CASCADE
	)
	plan_date = models.DateField()

	def __str__(self):
		return str(self.plan) + ' Date: ' + str(self.plan_date)


class PlanRouteDetail(models.Model):
	"""
	登山計画ルート詳細モデル
	登山計画ルートに対してルート詳細(経由地・宿泊地)を登録可能
	"""
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	created_user = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_route_detail_created_user',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_user = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_route_detail_updated_user',
		on_delete=models.CASCADE
	)
	updated_at = models.DateTimeField(auto_now=True)
	plan_route = models.ForeignKey(
		PlanRoute,
		related_name='plan_route_detail_plan_route',
		on_delete=models.CASCADE
	)
	name = models.CharField(max_length=50)
	is_staying = models.BooleanField(default=False)
	sort_index = models.IntegerField()

	def __str__(self):
		return str(self.plan_route) + ' Name: ' + str(self.name)


class PlanEscapeRoute(models.Model):
	"""
	登山計画エスケープルートモデル
	登山計画に対してエスケープルートを登録可能
	"""
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	created_user = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_escape_route_created_user',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_user = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_escape_route_updated_user',
		on_delete=models.CASCADE
	)
	updated_at = models.DateTimeField(auto_now=True)
	plan = models.OneToOneField(
		Plan,
		related_name='plan_escape_route_plan',
		on_delete=models.CASCADE
	)
	content = models.TextField(max_length=300, blank=True, null=True)

	def __str__(self):
		return str(self.plan)


class PlanMember(models.Model):
	"""
	登山計画メンバーモデル
	登山計画に対してメンバーを登録可能
	"""
	PREFECTURE = choices.PREFECTURE
	GENDER_TYPE = choices.GENDER_TYPE
	BLOOD_TYPE = choices.BLOOD_TYPE

	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	created_user = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_member_created_user',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_user = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_member_updated_user',
		on_delete=models.CASCADE
	)
	updated_at = models.DateTimeField(auto_now=True)
	plan = models.ForeignKey(
		Plan,
		related_name='plan_member_plan',
		on_delete=models.CASCADE
	)
	user = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='plan_member_user',
		on_delete=models.SET_NULL,
		blank=True,
		null=True
	)
	name = models.CharField(max_length=100)
	postal_code = models.CharField(max_length=8)
	prefecture = models.IntegerField(choices=PREFECTURE)
	address = models.CharField(max_length=200)
	gender_type = models.IntegerField(choices=GENDER_TYPE)
	blood_type = models.IntegerField(choices=BLOOD_TYPE)
	home_phone_number = models.CharField(max_length=13, blank=True, null=True)
	cell_phone_number = models.CharField(max_length=13, blank=True, null=True)
	emergency_contact_name = models.CharField(max_length=100)
	emergency_contact_phone = models.CharField(max_length=13)
	emergency_contact_email = models.CharField(
		max_length=100, blank=True, null=True)
	insurance_name = models.CharField(max_length=100, blank=True, null=True)
	insurance_number = models.CharField(max_length=100, blank=True, null=True)
	hitococo_id = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return str(self.plan) + ' Name: ' + str(self.name)


class Bookmark(models.Model):
	"""
	ブックマークモデル
	"""
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	user = models.ForeignKey(
		settings_core.AUTH_USER_MODEL,
		related_name='bookmark_user',
		on_delete=models.CASCADE
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	plan = models.ForeignKey(
		Plan,
		related_name='bookmark_plan',
		on_delete=models.CASCADE
	)

	class Meta:
		unique_together = (('user', 'plan'),)

	def __str__(self):
		return str(self.plan) + ' User: ' + str(self.user)
