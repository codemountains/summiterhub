from rest_framework import serializers
from .models import Plan, PlanGear, PlanCustomGear, PlanRoute, \
	PlanRouteDetail, PlanEscapeRoute, PlanMember, Bookmark
from utils.format import created_at, updated_at


class PlanSerializer(serializers.ModelSerializer):
	"""
	登山計画シリアライザ
	"""
	created_at = created_at()
	updated_at = updated_at()
	purpose_type_name = serializers.CharField(
		source='get_purpose_type_display',
		read_only=True
	)
	prefecture_name = serializers.CharField(
		source='get_prefecture_display',
		read_only=True
	)

	class Meta:
		model = Plan
		fields = [
			'id',
			'created_user',
			'created_at',
			'updated_user',
			'updated_at',
			'purpose_type',
			'purpose_type_name',
			'prefecture',
			'prefecture_name',
			'mountain_first',
			'mountain_second',
			'mountain_third',
			'mountain_fourth',
			'mountain_fifth',
			'is_submitted',
			'submitted_date',
			'entering_date',
			'descending_date',
			'affiliate_group_name',
			'affiliate_group_phone',
			'has_trail_snacks',
			'water_liters',
			'food_times',
			'emergency_food_times'
		]
		extra_kwargs = {
			'created_user': {'read_only': True},
			'updated_user': {'read_only': True}
		}


class PlanGearSerializer(serializers.ModelSerializer):
	"""
	登山計画装備シリアライザ
	"""
	created_at = created_at()
	updated_at = updated_at()
	riding_type_name = serializers.CharField(
		source='get_riding_type_display',
		read_only=True
	)

	class Meta:
		model = PlanGear
		fields = [
			'id',
			'created_user',
			'created_at',
			'updated_user',
			'updated_at',
			'plan',
			'has_rain_wear',
			'has_winter_clothing',
			'has_map',
			'has_compass',
			'has_headlamp',
			'has_mobile_phone',
			'has_spare_battery',
			'has_first_aid_kit',
			'has_emergency_tent',
			'has_transceiver',
			'call_sign',
			'has_radio',
			'has_tent',
			'has_sleeping_bag',
			'has_stove',
			'has_helmet',
			'has_climbing_rope',
			'has_climbing_gear',
			'has_crampons',
			'has_ice_axe',
			'has_shovel',
			'has_beacon',
			'has_probe',
			'has_snow_saw',
			'has_riding_gear',
			'riding_type',
			'riding_type_name'
		]
		extra_kwargs = {
			'created_user': {'read_only': True},
			'updated_user': {'read_only': True}
		}


class PlanCustomGearSerializer(serializers.ModelSerializer):
	"""
	登山計画カスタム装備シリアライザ
	"""
	created_at = created_at()
	updated_at = updated_at()

	class Meta:
		model = PlanCustomGear
		fields = [
			'id',
			'created_user',
			'created_at',
			'updated_user',
			'updated_at',
			'plan',
			'name',
			'sort_index'
		]
		extra_kwargs = {
			'created_user': {'read_only': True},
			'updated_user': {'read_only': True}
		}


class PlanRouteSerializer(serializers.ModelSerializer):
	"""
	登山計画ルートシリアライザ
	"""
	created_at = created_at()
	updated_at = updated_at()

	class Meta:
		model = PlanRoute
		fields = [
			'id',
			'created_user',
			'created_at',
			'updated_user',
			'updated_at',
			'plan',
			'plan_date'
		]
		extra_kwargs = {
			'created_user': {'read_only': True},
			'updated_user': {'read_only': True}
		}


class PlanRouteDetailSerializer(serializers.ModelSerializer):
	"""
	登山計画ルート詳細シリアライザ
	"""
	created_at = created_at()
	updated_at = updated_at()

	class Meta:
		model = PlanRouteDetail
		fields = [
			'id',
			'created_user',
			'created_at',
			'updated_user',
			'updated_at',
			'plan_route',
			'name',
			'is_staying',
			'sort_index'
		]
		extra_kwargs = {
			'created_user': {'read_only': True},
			'updated_user': {'read_only': True}
		}


class PlanEscapeRouteSerializer(serializers.ModelSerializer):
	"""
	登山計画エスケープルートシリアライザ
	"""
	created_at = created_at()
	updated_at = updated_at()

	class Meta:
		model = PlanEscapeRoute
		fields = [
			'id',
			'created_user',
			'created_at',
			'updated_user',
			'updated_at',
			'plan',
			'content'
		]
		extra_kwargs = {
			'created_user': {'read_only': True},
			'updated_user': {'read_only': True}
		}


class PlanMemberSerializer(serializers.ModelSerializer):
	"""
	登山計画メンバーシリアライザ
	"""
	created_at = created_at()
	updated_at = updated_at()
	prefecture_name = serializers.CharField(
		source='get_prefecture_display',
		read_only=True
	)
	gender_type_name = serializers.CharField(
		source='get_gender_type_display',
		read_only=True
	)
	blood_type_name = serializers.CharField(
		source='get_blood_type_display',
		read_only=True
	)

	class Meta:
		model = PlanMember
		fields = [
			'id',
			'created_user',
			'created_at',
			'updated_user',
			'updated_at',
			'plan',
			'user',
			'name',
			'postal_code',
			'prefecture',
			'prefecture_name',
			'address',
			'gender_type',
			'gender_type_name',
			'blood_type',
			'blood_type_name',
			'home_phone_number',
			'cell_phone_number',
			'emergency_contact_name',
			'emergency_contact_phone',
			'emergency_contact_email',
			'insurance_name',
			'insurance_number',
			'hitococo_id',
		]
		extra_kwargs = {
			'created_user': {'read_only': True},
			'updated_user': {'read_only': True}
		}


class BookmarkSerializer(serializers.ModelSerializer):
	"""
	ブックマークシリアライザ
	"""
	created_at = created_at()
	updated_at = updated_at()

	class Meta:
		model = Bookmark
		fields = [
			'id',
			'user',
			'created_at',
			'updated_at',
			'plan',
		]
		extra_kwargs = {
			'user': {'read_only': True}
		}


class PlanSearchSerializer(serializers.ModelSerializer):
	"""
	登山計画検索シリアライザ
	"""
	purpose_type_name = serializers.CharField(
		source='get_purpose_type_display',
		read_only=True
	)
	prefecture_name = serializers.CharField(
		source='get_prefecture_display',
		read_only=True
	)

	class Meta:
		model = Plan
		fields = [
			'id',
			'purpose_type',
			'purpose_type_name',
			'prefecture',
			'prefecture_name',
			'mountain_first',
			'mountain_second',
			'mountain_third',
			'mountain_fourth',
			'mountain_fifth',
			'entering_date',
			'descending_date'
		]
