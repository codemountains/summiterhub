from rest_framework import serializers
from .models import News, ReadNews
from utils.format import created_at, updated_at


class NewsSerializer(serializers.ModelSerializer):
	"""
	ニュースシリアライザ
	"""
	created_at = created_at()
	updated_at = updated_at()

	class Meta:
		model = News
		fields = [
			'id',
			'created_at',
			'updated_at',
			'title',
			'content',
			'attached_image'
		]
		extra_kwargs = {
			'is_active': {'read_only': True},
			'title': {'read_only': True},
			'content': {'read_only': True},
			'attached_image': {'read_only': True}
		}


class ReadNewsSerializer(serializers.ModelSerializer):
	"""
	既読ニュースシリアライザ
	"""
	created_at = created_at()
	updated_at = updated_at()

	class Meta:
		model = ReadNews
		fields = [
			'id',
			'user_id',
			'created_at',
			'updated_at',
			'news_id'
		]
		extra_kwargs = {
			'user_id': {'read_only': True},
			'is_active': {'read_only': True}
		}
