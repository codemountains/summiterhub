from django.db.models import Q
from rest_framework import status, generics, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .serializers import PlanSerializer, PlanGearSerializer, \
	PlanCustomGearSerializer, PlanRouteSerializer, PlanRouteDetailSerializer, \
	PlanEscapeRouteSerializer, PlanMemberSerializer, BookmarkSerializer
from .models import Plan, PlanGear, PlanCustomGear, PlanRoute, \
	PlanRouteDetail, PlanEscapeRoute, PlanMember, Bookmark


class PlanViewSet(viewsets.ModelViewSet):
	"""
	登山計画 ModelViewSet
	"""
	serializer_class = PlanSerializer
	queryset = Plan.objects.all()

	def get_queryset(self):
		return self.queryset.filter(created_user_id=self.request.user)

	def perform_create(self, serializer):
		serializer.save(created_user_id=self.request.user, updated_user_id=self.request.user)

	def perform_update(self, serializer):
		serializer.save(updated_user_id=self.request.user)

	# def perform_destroy(self, instance):
	# 	instance.is_active = False
	# 	instance.updated_user_id = self.request.user
	# 	instance.save()


class PlanGearViewSet(viewsets.ModelViewSet):
	"""
	登山計画装備 ModelViewSet
	"""
	serializer_class = PlanGearSerializer
	queryset = PlanGear.objects.all()

	def get_queryset(self):
		return self.queryset.filter(plan_id_id=self.kwargs.get('plan_id'))

	def perform_create(self, serializer):
		serializer.save(created_user_id=self.request.user, updated_user_id=self.request.user)

	def perform_update(self, serializer):
		serializer.save(updated_user_id=self.request.user)


class PlanCustomGearViewSet(viewsets.ModelViewSet):
	"""
	登山計画カスタム装備 ModelViewSet
	"""
	serializer_class = PlanCustomGearSerializer
	queryset = PlanCustomGear.objects.all()

	def get_queryset(self):
		return self.queryset.filter(plan_id_id=self.kwargs.get('plan_id'))

	def perform_create(self, serializer):
		serializer.save(created_user_id=self.request.user, updated_user_id=self.request.user)

	def perform_update(self, serializer):
		serializer.save(updated_user_id=self.request.user)


class PlanRouteViewSet(viewsets.ModelViewSet):
	"""
	登山計画ルート ModelViewSet
	"""
	serializer_class = PlanRouteSerializer
	queryset = PlanRoute.objects.all()

	def get_queryset(self):
		return self.queryset.filter(plan_id_id=self.kwargs.get('plan_id'))

	def perform_create(self, serializer):
		serializer.save(created_user_id=self.request.user, updated_user_id=self.request.user)

	def perform_update(self, serializer):
		serializer.save(updated_user_id=self.request.user)


class PlanRouteDetailViewSet(viewsets.ModelViewSet):
	"""
	登山計画ルート詳細 ModelViewSet
	"""
	serializer_class = PlanRouteDetailSerializer
	queryset = PlanRouteDetail.objects.all()

	def get_queryset(self):
		return self.queryset.filter(plan_route_id_id=self.kwargs.get('plan_route_id'))

	def perform_create(self, serializer):
		serializer.save(created_user_id=self.request.user, updated_user_id=self.request.user)

	def perform_update(self, serializer):
		serializer.save(updated_user_id=self.request.user)


class PlanEscapeRouteViewSet(viewsets.ModelViewSet):
	"""
	登山計画エスケープルート ModelViewSet
	"""
	serializer_class = PlanEscapeRouteSerializer
	queryset = PlanEscapeRoute.objects.all()

	def get_queryset(self):
		return self.queryset.filter(plan_id_id=self.kwargs.get('plan_id'))

	def perform_create(self, serializer):
		serializer.save(created_user_id=self.request.user, updated_user_id=self.request.user)

	def perform_update(self, serializer):
		serializer.save(updated_user_id=self.request.user)


class BookmarkViewSet(viewsets.ModelViewSet):
	"""
	ブックマーク ModelViewSet
	"""
	serializer_class = BookmarkSerializer
	queryset = Bookmark.objects.all()

	def get_queryset(self):
		return self.queryset.filter(user_id=self.request.user)

	def perform_create(self, serializer):
		try:
			serializer.save(user_id=self.request.user)
		except BaseException:
			raise ValidationError('You\'ve already bookmarked this plan.')

	def update(self, request, *args, **kwargs):
		response = {'message': 'PUT method is not allowed.'}
		return Response(response, status=status.HTTP_400_BAD_REQUEST)

	def partial_update(self, request, *args, **kwargs):
		response = {'message': 'PATCH method is not allowed.'}
		return Response(response, status=status.HTTP_400_BAD_REQUEST)
