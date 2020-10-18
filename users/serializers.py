from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserDetail, Friend, FriendRequest, BlockingFriend, \
	Party, PartyMember


class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=False)

	class Meta:
		model = get_user_model()
		fields = ['id', 'email', 'password']
		extra_kwargs = {
			'password': {'write_only': True, 'required': True}
		}

	def create(self, validated_data):
		user = get_user_model().objects.create_user(**validated_data)
		return user

	def update(self, instance, validated_data):
		if 'password' in validated_data:
			instance.set_password(validated_data['password'])
		else:
			instance = super().update(instance, validated_data)
		instance.save()
		return instance

	def __delete__(self, instance):
		instance.is_active = False
		instance.save()


class UserDetailSerializer(serializers.ModelSerializer):
	created_at = serializers.DateTimeField(
		format="%Y-%m-%d %H:%M",
		read_only=True
	)
	updated_at = serializers.DateTimeField(
		format="%Y-%m-%d %H:%M",
		read_only=True
	)
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
		model = UserDetail
		fields = [
			'id',
			'user_id',
			'created_at',
			'updated_at',
			'is_active',
			'profile_name',
			'profile_image',
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
			'user_id': {'read_only': True}
		}
