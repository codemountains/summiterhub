from rest_framework import serializers
from .models import Gear, CustomGear
from utils.format import created_at, updated_at


class GearSerializer(serializers.ModelSerializer):
	"""
	装備シリアライザ
	"""
	created_at = created_at()
	updated_at = updated_at()
	purpose_type_name = serializers.CharField(
		source='get_purpose_type_display',
		read_only=True
	)
	riding_type_name = serializers.CharField(
		source='get_riding_type_display',
		read_only=True
	)

	class Meta:
		model = Gear
		fields = [
			'id',
			'user_id',
			'created_at',
			'updated_at',
			'title',
			'purpose_type',
			'purpose_type_name',
			'remarks',
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
			'user_id': {'read_only': True}
		}


class CustomGearSerializer(serializers.ModelSerializer):
	"""
	カスタム装備シリアライザ
	"""
	created_at = created_at()
	updated_at = updated_at()

	class Meta:
		model = CustomGear
		fields = [
			'id',
			'user_id',
			'created_at',
			'updated_at',
			'gear_id',
			'name',
			'sort_index'
		]
		extra_kwargs = {
			'user_id': {'read_only': True},
			'gear_id': {'read_only': True}
		}
