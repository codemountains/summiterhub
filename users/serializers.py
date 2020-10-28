from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserDetail, UserToken, Friend, FriendRequest, \
	BlockingFriend, Party, PartyMember
from utils.format import created_at, updated_at, expiration_at


class UserSerializer(serializers.ModelSerializer):
	"""
	ユーザシリアライザ
	"""
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


class UserTokenSerializer(serializers.ModelSerializer):
	created_at = created_at()
	expiration_at = expiration_at()

	class Meta:
		model = UserToken
		fields = [
			'id',
			'user',
			'email',
			'token',
			'created_at',
			'expiration_at'
		]
		extra_kwargs = {
			'user': {'read_only': True},
			'email': {'read_only': True},
			'token': {'read_only': True}
		}


class UserDetailSerializer(serializers.ModelSerializer):
	"""
	ユーザ詳細シリアライザ
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
		model = UserDetail
		fields = [
			'id',
			'user',
			'created_at',
			'updated_at',
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
			'user': {'read_only': True}
		}


class FriendRequestSerializer(serializers.ModelSerializer):
	"""
	フレンド申請シリアライザ
	"""
	created_at = created_at()
	updated_at = updated_at()
	status_type_name = serializers.CharField(
		source='get_status_type_display',
		read_only=True
	)

	class Meta:
		model = FriendRequest
		fields = [
			'id',
			'src_user',
			'dest_email',
			'dest_user',
			'created_at',
			'updated_at',
			'message',
			'status_type',
			'status_type_name'
		]
		extra_kwargs = {
			'src_user': {'read_only': True}
		}


class FriendSerializer(serializers.ModelSerializer):
	"""
	フレンドシリアライザ
	"""
	created_at = created_at()
	updated_at = updated_at()

	class Meta:
		model = Friend
		fields = [
			'id',
			'src_user',
			'dest_user',
			'created_at',
			'updated_at',
			'friend_request_id'
		]
		extra_kwargs = {
			'src_user': {'read_only': True},
			'dest_user': {'read_only': True}
		}


class BlockingFriendSerializer(serializers.ModelSerializer):
	"""
	ブロックフレンドシリアライザ
	"""
	created_at = created_at()
	updated_at = updated_at()

	class Meta:
		model = BlockingFriend
		fields = [
			'id',
			'src_user',
			'dest_user',
			'created_at',
			'updated_at',
		]
		extra_kwargs = {
			'src_user': {'read_only': True}
		}


class PartySerializer(serializers.ModelSerializer):
	"""
	パーティシリアライザ
	"""
	created_at = created_at()
	updated_at = updated_at()

	class Meta:
		model = Party
		fields = [
			'id',
			'user',
			'created_at',
			'updated_at',
			'name',
			'remarks'
		]
		extra_kwargs = {
			'user': {'read_only': True}
		}


class PartyMemberSerializer(serializers.ModelSerializer):
	"""
	パーティメンバーシリアライザ
	"""
	created_at = created_at()
	updated_at = updated_at()

	class Meta:
		model = PartyMember
		fields = [
			'id',
			'user',
			'created_at',
			'updated_at',
			'party',
			'entry_user',
			'sort_index'
		]
		extra_kwargs = {
			'user': {'read_only': True},
			'party': {'read_only': True}
		}
