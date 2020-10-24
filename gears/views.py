from django.db.models import Q
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from .serializers import GearSerializer, CustomGearSerializer
from .models import Gear, CustomGear


class GearViewSet(viewsets.ModelViewSet):
	"""
	装備 ModelViewSet
	"""
	serializer_class = GearSerializer
	queryset = Gear.objects.all()

	# 自分の装備のみが操作対象
	def get_queryset(self):
		return self.queryset.filter(user_id=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user_id=self.request.user)


class CustomGearViewSet(viewsets.ModelViewSet):
	"""
	カスタム装備 ModelViewSet
	"""
	serializer_class = CustomGearSerializer
	queryset = CustomGear.objects.all()

	# 自分の装備のみが操作対象
	def get_queryset(self):
		return self.queryset.filter(
			Q(gear_id_id=self.kwargs.get('gear_id'))
			&
			Q(gear_id__user_id=self.request.user)
		)

	def perform_create(self, serializer):
		gear = self.queryset.filter(gear_id_id=self.kwargs.get('gear_id')).first()
		if gear.user_id != self.request.user:
			raise ValidationError('カスタム装備の作成権限がありません')

		serializer.save(
			user_id=self.request.user,
			gear_id_id=self.kwargs.get('gear_id')
		)
